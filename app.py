import pickle
import pandas as pd
import numpy as np
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
from PaDEL_pywrapper import PaDEL
from PaDEL_pywrapper import descriptors

st.title("Test de ML para ligando-receptor")

smile = st.input("Ingresa tu molécula en código SMILES: ", 
                 "c1cccc(NC2=O)c1[C@]23[C@@H]4c5n([C@H](C3)C(=O)N4)c(=O)c6c(n5)cccc6")

df = pd.DataFrame({'smiles': [smile]})
st.show(df)

# Load selected features
with open("RDKit_select_descriptors.pickle", "rb") as f:
    RDKit_select_descriptors = pickle.load(f)

with open("PaDEL_select_descriptors.pickle", "rb") as f:
    PaDEL_select_descriptors = pickle.load(f)

# Load the saved scalers
with open("robust_scaler.pickle", "rb") as f:
    robust_scaler = pickle.load(f)

with open("minmax_scaler.pickle", "rb") as f:
    minmax_scaler = pickle.load(f)

# Load RFE model
with open("selector_LGBM.pickle", "rb") as f:
    selector_lgbm = pickle.load(f)

# Load the trained model
with open("lgbm_best_model.pickle", "rb") as f:
    lgbm_model = pickle.load(f)

# RDKit selected descriptors function
def get_selected_RDKitdescriptors(smile, selected_descriptors, missingVal=None):
    ''' Calculates only the selected descriptors for a molecule '''
    res = {}
    mol = Chem.MolFromSmiles(smile)
    if mol is None:
        return {desc: missingVal for desc in selected_descriptors}

    for nm, fn in Descriptors._descList:
        if nm in selected_descriptors:
            try:
                res[nm] = fn(mol)
            except:
                import traceback
                traceback.print_exc()
                res[nm] = missingVal
    return res
