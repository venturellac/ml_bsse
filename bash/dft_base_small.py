from pyscf.pbc import gto, dft, scf, df
from pyscf.pbc.lib import chkfile
import os
import numpy as np
import scipy
from libdmet_solid.utils.misc import read_poscar

cell = gto.Cell()
cell = read_poscar(fname=
cell.basis = 'def2-svp'
cell.max_memory = 180000
cell.precision = 1e-10
cell.spin = 0
cell.charge = 0
cell.verbose = 5
cell.build()

from pyscf.pbc.tools import k2gamma
kpts = cell.make_kpts([1,1,1])
cell, phase = k2gamma.get_phase(cell, kpts)

gdf = df.RSDF(cell)
gdf_fname = 'gdf_ints.h5'
gdf.auxbasis = 'def2-svp-ri'
gdf._cderi_to_save = gdf_fname
if not os.path.isfile(gdf_fname):
    gdf.build()

chkfname = 
if os.path.isfile(chkfname):
    kmf = dft.RKS(cell).rs_density_fit()
    kmf = scf.addons.smearing_(kmf, sigma=5e-3, method='fermi')
    kmf.xc = 'rpbe'
    kmf.exxdiv = None
    kmf.with_df = gdf
    kmf.with_df._cderi = gdf_fname
    data = chkfile.load(chkfname, 'scf')
    kmf.__dict__.update(data)
else:
    kmf = dft.RKS(cell).rs_density_fit()
    kmf = scf.addons.smearing_(kmf, sigma=5e-3, method='fermi')
    kmf.xc = 'rpbe'
    kmf.exxdiv = None
    kmf.with_df = gdf
    kmf.with_df._cderi = gdf_fname
    kmf.conv_tol = 1e-10
    kmf.max_cycle = 200
    kmf.chkfile = chkfname
    kmf.diis_space = 15
    kmf.diis_damp = 0.9
    kmf.init_guess = 'atom'
    kmf.kernel()

print('RPBE total energy:', kmf.e_tot)
