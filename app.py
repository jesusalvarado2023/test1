import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

st.title("Test de ML para ligando-receptor")

compound_smiles=st.text_input('Ingresa tu código SMILES','FCCC(=O)[O-]')
m = Chem.MolFromSmiles(compound_smiles)

Draw.MolToFile(m,'mol.png')
st.image('mol.png')
