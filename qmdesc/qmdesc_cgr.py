# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:50:12 2021

@author: jerryyao
"""

import rdkit
import qmdesc
import numpy as np
from CGRtools.files import*
from CGRtools.containers import*
from CGRtools import smiles
from CGRtools.utils import *

class qmdesc_cgr():
    def __init__(self,explicify_h=False):
        self.explicify_h=explicify_h
        self.handler=qmdesc.handler.ReactivityDescriptorHandler()
    def predict(self,cgrmol):
        self.cgrmol=cgrmol
        if self.explicify_h:
            self.cgrmol.explicify_hydrogens()
        self.rdmol=to_rdkit_molecule(self.cgrmol)
        self.qmdesc=self.handler.predict_mol(self.rdmol)
        self.bond_list=list(self.cgrmol.bonds())
        for i in range(len(self.bond_list)):
            self.bond_list[i]=list(self.bond_list[i])
            if self.bond_list[i][0]>self.bond_list[i][1]:
                bond_tem=self.bond_list[i][0]
                self.bond_list[i][0]=self.bond_list[i][1]
                self.bond_list[i][1]=bond_tem
        self.qmdesc['bond_index']=self.bond_list
        self.qmdesc['atom_index']=list(self.cgrmol.atoms())
        return self.qmdesc