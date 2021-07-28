# qmdesc

[![GitHub license](https://img.shields.io/github/license/yanfeiguan/qmdesc)](https://github.com/yanfeiguan/qmdesc/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/qmdesc/badge/?version=latest)](https://qmdesc.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/qmdesc.svg)](https://badge.fury.io/py/qmdesc)


A trained multitask constraint message passing neural networks 
for QM atomic/bond property predictions as described in the paper 
[Regio-Selectivity Prediction with a Machine-Learned Reaction Representation and On-the-Fly Quantum Mechanical Descriptors](https://doi.org/10.26434/chemrxiv.12907316.v1).

QM descriptors under B3LYP/def2svp level of theory that can be predicted with this model:
1. Hirshfeld partial charge
2. Neucleuphilic Fukui indices
3. Electrophilic Fukui indices
4. NMR shielding constants
5. Bond lengths
6. Bond orders

**Documentation:** Documentation of qmdesc is available at https://qmdesc.readthedocs.io/en/latest/index.html.

## Requirements

* RDKit
* CGRtools

### Installation
For all installations, we recommend using conda to get the necessary rdkit dependency:
```console
conda install -c rdkit rdkit
pip install qmdesc
```

Or from envrioment.yml 
```console
conda create --name qmdesc --file environment.yml
```
### Usage
```console
import rdkit
import qmdesc
import numpy as np
from CGRtools.files import*
from CGRtools.containers import*
from CGRtools import smiles
from CGRtools.utils import *
smiles2='Br[c:4]1[cH:3][c:1]2[c:25]([nH:15][c:16]3[cH:17][cH:18][c:19](Br)[cH:32][c:33]23)[cH:24][cH:23]1.OB(O)[c:26]1[cH:27][cH:28][cH:29][cH:30][cH:31]1>>[cH:1]1[cH:2][cH:3][c:4](-[c:5]2[cH:6][cH:7][cH:8][cH:9][c:10]2-[c:11]2[cH:12][cH:13][c:14]3[nH:15][c:16]4[cH:17][cH:18][c:19](-[c:20]5[cH:21][cH:22][cH:23][cH:24][c:25]5-[c:26]5[cH:27][cH:28][cH:29][cH:30][cH:31]5)[cH:32][c:33]4[c:34]3[cH:35]2)[cH:36][cH:37]1'
cgr=smiles(smiles2)
cgr.explicify_hydrogens()
cgr_mol=cgr.reactants[0]
qm=qmdesc_cgr()
result=qm.predict(cgr_mol)
```

