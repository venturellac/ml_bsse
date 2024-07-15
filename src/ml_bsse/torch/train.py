

import torch
import torch.nn as nn
import torch.nn.functional as F

# you need to figure out the best way to create datasets from your Copper systems (probably each system is a Data object, the list of them is the Dataset object), the below link has details
# https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader
from torch.utils.data import DataLoader, Dataset

import torch.optim as optim
from torch.optim.lr_scheduler import StepLR, CyclicLR, ExponentialLR, LambdaLR, ChainedScheduler, CosineAnnealingWarmRestarts

from torch.func import stack_module_state
from torch.func import functional_call
from torch import vmap

def count_parameters(model):
    # A function to print the number of parameters for each submodule
    def get_num_params(module, prefix=''):
        total_params = 0
        for name, submodule in module.named_children():
            submodule_params = sum(p.numel() for p in submodule.parameters())
            submodule_prefix = f"{prefix}.{name}" if prefix else name
            # print(f"{submodule_prefix}: {submodule_params} params")
            total_params += submodule_params

            # Recursively count params for submodules, handling ModuleList and Sequential
            if isinstance(submodule, (nn.ModuleList, nn.Sequential)):
                for idx, sm in enumerate(submodule):
                    sm_prefix = f"{submodule_prefix}[{idx}]"
                    total_params += get_num_params(sm, sm_prefix)
            else:
                total_params += get_num_params(submodule, submodule_prefix)
                
        return total_params

    tot_params = get_num_params(model)
    return tot_params


def setup_seed(seed):
    random.seed(seed)                          
    np.random.seed(seed)                       
    torch.manual_seed(seed)                    
    torch.cuda.manual_seed(seed)               
    torch.cuda.manual_seed_all(seed)           
    torch.backends.cudnn.deterministic = True 

def train_model(dataset, model, train_config, seed = 42, loss_kwargs = {}, rank = 0, log_dir = None, dos_monitor = None):
    setup_seed(seed)
    device =  train_config.get('device', None)
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if device == 'cuda' and not torch.cuda.is_available():
        warnings.warn('device cuda requested but cuda not available, using CPU')
        device = 'cpu'

    if rank == 0:
        print('train_config: ', train_config, flush = True)
        print('loss_kwargs: ', loss_kwargs, flush = True)
        print('Device used for training: ', device, flush = True)
        total_num_params = count_parameters(model)
        print('Model total number of params: ', total_num_params, flush = True)

    model.to(device)

    n_epochs = int(train_config.get('epochs', None))
    if n_epochs is None:
        n_epochs = int(train_config.get('steps', 1000))

    weight_decay = train_config.get('weight_decay', 0.0)
    learning_rate = train_config.get('learning_rate', 0.001)
    batch_size = train_config.get('batch_size', np.inf) # the number of molecules per backward pass
    ndata = len(dataset)
    batch_size = min(batch_size, ndata)

    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    shuffle = train_config.get('shuffle', False)
    num_workers = train_config.get('num_workers', 0)
    pin_memory = train_config.get('pin_memory', True)


    loss_kwargs['rank'] = rank
    loss_kwargs['device'] = device
    loss_kwargs['batch_size'] = batch_size
    loss_kwargs['omega_fit'] = data[0].iomega


    if not log_dir is None and rank == 0:
        writer = SummaryWriter(log_dir=log_dir)

    loader = DataLoader(dataset, batch_size = batch_size, shuffle = shuffle, pin_memory=pin_memory, num_workers = num_workers) #, worker_init_fn = seed
    
    for epoch in range(n_epochs):
        t0 = time.time()
        for b, batch in enumerate(loader):
            optimizer.zero_grad()   # zero the gradient buffers
            loss = 0
            batch = batch.to(device) # , non_blocking=True

            for i in range(len(batch)):
                mol = batch[i]
                bsse_ml = model(mol, train = True)
                bsse_true = mol.bsse_true
                loss += (bsse_ml - bsse_true)**2

            loss.backward()
            optimizer.step()    # Does the update

        # write log
        if rank == 0:
            t1 = time.time()
            t = t1-t0
            if loss != 0:
                loss_val = loss.detach().cpu().numpy()
            else:
                loss_val = -1 # means the loss was not computed in the final batch
            print(f'time for Adam #{epoch}: {t:0.2f}s, main loop value (final batch loss): {loss_val:0.6e}', flush = True) # , big_loss_count: {big_loss_count}

    return model
