import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import io

import warnings
warnings.filterwarnings('ignore')


def main():
    st.write("testo prova")
    #creo le tre variabili di input da inserire
    st.title("REGRESSIONE LINEARE")
    rd=st.number_input("inserisci il valore di R&D Spend",1,1000,500)
    adm=st.number_input("inserisci il valore di Administration",1,1000,500)
    mkt=st.number_input("inserisci il valore di Marketing_Spend",1,1000,500)
    df=pd.read_csv("https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv",sep=",")
    buffer = io.BytesIO()

    newmodel = joblib.load('regression_test.pkl') ## to load model, carico il modello 
    res=newmodel.predict([[rd,adm,mkt]])[0] #faccio inferenza con il nuovo modello, ossia previsione inserendo 3 input
    st.write("Il profitto previsto è pari ad € ",round(res,1)) #stampo il modello

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.

        df.to_excel(writer, sheet_name='Sheet1', index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()
        download2 = st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='large_df.xlsx',
            mime='application/vnd.ms-excel'
        )



    
if __name__ == "__main__":
    main()
#scrivere in terminale la prima volta : python -m streamlit run app.py 