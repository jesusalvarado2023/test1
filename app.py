import pandas as pd
import numpy as np
import streamlit as st

st.title("Test de ML para ligando-receptor")

smile = st.input("Ingresa tu molécula en código SMILES: ", 
                 "c1cccc(NC2=O)c1[C@]23[C@@H]4c5n([C@H](C3)C(=O)N4)c(=O)c6c(n5)cccc6")

df = pd.DataFrame({'smiles': [smile]})
st.show(df)

