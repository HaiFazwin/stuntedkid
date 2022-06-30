import streamlit as st
import pandas as pd

st.write("""
# Influenza Test

This app predicts the **Influenza Test** type!
""")

st.sidebar.header('How are you?')

def user_input_features():
    Temperature = st.sidebar.slider('Your Temperature', 35, 36, 37,38,39,40,41,42,43,44)
    RunningNose = st.sidebar.slider('Running Nose?', 1, 0)
    Cough = st.sidebar.slider('Coughing?',1, 0)
    Dizziness = st.sidebar.slider('Dizziness?', 1, 0)
    data = {'Temperature': Your Temperature,
            'RunningNose': Running Nose?,
            'Cough': Coughing?,
            'Dizziness': Dizziness?}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/HaiFazwin/stuntedkid/main/Influenza%20-%20Sheet1%20(1).csv')
X = iris.drop('Result',axis=1)
Y = iris.Result

st.subheader('Class labels and their corresponding index number')
st.write(['Positive','Negatif'])

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
