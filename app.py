# importo le librerie 
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import joblib
import io


# implemento la funzione main
def main():

   
    

    # caricamento del modello 
    
    new_model = joblib.load('regression_test.pkl') ## to load model, carico il modello 
    

    
    st.header("Input values")
    Adult_Mortality = st.number_input('Enter a NUMBER value Adult Mortality:', 1,1000,263)
    BMI = st.number_input('Enter a NUMBER value BMI:',1,100,19)
    Polio = st.number_input('Enter a NUMBER value Polio:',1,100,6)
    Diphteria = st.number_input('Enter a NUMBER value Diphteria:',1,100,65)
    HIV = st.number_input('Enter a NUMBER value hiv:',0,10,0)
    # value=0.46, step=0.01, min_value=0.46, max_value=27.74
    Income = st.number_input('Enter a NUMBER value Income:',0,10,0)
    Schooling = st.number_input('Enter a NUMBER value Schooling:',1,100,10)
  
    # predizione dei valori dati in input
    st.write("Y_PRED: ",round(new_model.predict([[Adult_Mortality,BMI,Polio,Diphteria,HIV,Income,Schooling]])[0],2))

    # carico file csv
    uploaded_file = st.file_uploader("Inserisci il csv di input")
    
    # verifico che il file non sia vuoto
    if uploaded_file is not None:
        df = pd.DataFrame()

        # se non carico un file csv lancio un warning a video
        if uploaded_file.name[-3:] != "csv":
            st.warning("CSV file is required.")
        

        else:
            # leggo il csv e splitto in X e y 
            df = pd.read_csv(uploaded_file)

            X = df.drop(columns=['Life_exp','Measles ','Country','Year','infant deaths', 'percentage expenditure', 'Hepatitis B','under-five deaths ',' thinness  1-19 years',' thinness 5-9 years'])
            y = df['Life_exp']

            y_pred = new_model.predict(X)

            # creo il dataframe da scaricare con X_test e aggiungendo una nuova colonna "predict" y_pred
            df1 = df
            df1['real']=y
            df1["Predict"] = y_pred


            # bottone per scaricare X_test + y_pred
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df1.to_excel(writer, index=False)
                writer.save()
                st.download_button(
                    label="Download Excel Result",
                    data=buffer,
                    file_name="trasnformed_file.xlsx",
                    mime="application/vnd.ms-excel")
    

# questo modulo sarà eseguito solo se runnato
if __name__ == "__main__":
    main()
#scrivere in terminale la prima volta : python -m streamlit run app.py 