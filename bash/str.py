import numpy as np
from copy import deepcopy
from ase.build import fcc111, add_adsorbate
from ase.io.vasp import write_vasp

######### 441 #########
slab = fcc111('Cu', size=(4,4,1), a=3.615, vacuum=15.0)   # https://doi.org/10.1107/S0567739469001549

# Ontop
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.5+i*0.5, 'ontop', offset=2)
	add_adsorbate(slab_co, 'O', 2.628+i*0.5, 'ontop', offset=2)   # NIST website
	write_vasp('CO_Cu111_441_ontop_'+str(1.5+i*0.5)+'.vasp', slab_co)

# Bridge
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'bridge', offset=2)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'bridge', offset=2)   # NIST website
	write_vasp('CO_Cu111_441_bridge_'+str(1.0+i*0.5)+'.vasp', slab_co)

# FCC
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'fcc', offset=2)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'fcc', offset=2)   # NIST website
	write_vasp('CO_Cu111_441_fcc_'+str(1.0+i*0.5)+'.vasp', slab_co)

# HCP
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'hcp', offset=2)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'hcp', offset=2)   # NIST website
	write_vasp('CO_Cu111_441_hcp_'+str(1.0+i*0.5)+'.vasp', slab_co)

######### 332 #########
slab = fcc111('Cu', size=(3,3,2), a=3.615, vacuum=15.0)   # https://doi.org/10.1107/S0567739469001549

# Ontop
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.5+i*0.5, 'ontop', offset=1)
	add_adsorbate(slab_co, 'O', 2.628+i*0.5, 'ontop', offset=1)   # NIST website
	write_vasp('CO_Cu111_332_ontop_'+str(1.5+i*0.5)+'.vasp', slab_co)

# Bridge
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'bridge', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'bridge', offset=1)   # NIST website
	write_vasp('CO_Cu111_332_bridge_'+str(1.0+i*0.5)+'.vasp', slab_co)

# FCC
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'fcc', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'fcc', offset=1)   # NIST website
	write_vasp('CO_Cu111_332_fcc_'+str(1.0+i*0.5)+'.vasp', slab_co)

# HCP
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'hcp', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'hcp', offset=1)   # NIST website
	write_vasp('CO_Cu111_332_hcp_'+str(1.0+i*0.5)+'.vasp', slab_co)

######### 223 #########
slab = fcc111('Cu', size=(2,2,3), a=3.615, vacuum=15.0)   # https://doi.org/10.1107/S0567739469001549

# Ontop
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.5+i*0.5, 'ontop', offset=1)
	add_adsorbate(slab_co, 'O', 2.628+i*0.5, 'ontop', offset=1)   # NIST website
	write_vasp('CO_Cu111_223_ontop_'+str(1.5+i*0.5)+'.vasp', slab_co)

# Bridge
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'bridge', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'bridge', offset=1)   # NIST website
	write_vasp('CO_Cu111_223_bridge_'+str(1.0+i*0.5)+'.vasp', slab_co)

# FCC
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'fcc', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'fcc', offset=1)   # NIST website
	write_vasp('CO_Cu111_223_fcc_'+str(1.0+i*0.5)+'.vasp', slab_co)

# HCP
for i in range(10):
	slab_co = deepcopy(slab)
	add_adsorbate(slab_co, 'C', 1.0+i*0.5, 'hcp', offset=1)
	add_adsorbate(slab_co, 'O', 2.128+i*0.5, 'hcp', offset=1)   # NIST website
	write_vasp('CO_Cu111_223_hcp_'+str(1.0+i*0.5)+'.vasp', slab_co)
