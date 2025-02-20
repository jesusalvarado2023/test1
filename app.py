import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from PaDEL_pywrapper import PaDEL
from PaDEL_pywrapper import descriptors
import numpy as np

st.title("Test de ML para ligando-receptor")

compound_smiles=st.text_input('Ingresa tu código SMILES','FCCC(=O)[O-]')
m = Chem.MolFromSmiles(compound_smiles)

Draw.MolToFile(m,'mol.png')
st.image('mol.png')

#######
rdkit_archivo = joblib.load('./archivos/RDKit_select_descriptors.pickle')
padel_archivo = joblib.load('./archivos/PaDEL_select_descriptors.pickle')
