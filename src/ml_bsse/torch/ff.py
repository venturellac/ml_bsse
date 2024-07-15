import torch
import torch.nn as nn
import torch.nn.functional as F

import os
import numpy as np
import random
import argparse
import joblib
import time
import warnings
import psutil

# a wrapper around the nn.Module class so arbitrary **kwargs can be passed to each of the following models
# you can just add new models here of any name, just make sure you create an alias and add it to the pt_alias.py function
# this is so you can pass torch.nn models between the PyTorchModel or json specifications without ever having to pickle a pytorch object
class TorchBase(nn.Module):
    def __init__(self, **kwargs): 
        super(TorchBase, self).__init__()
        pass


class BPNN(TorchBase):
    def __init__(self, **kwargs):
        super(BPNN, self).__init__(**kwargs)

        # all the components go here

    def forward(self, mol, **kwargs):
        # each atom SOAP features go through a FF NN that returns atomwsie energy contributions

        # sum the atom-wise energies


