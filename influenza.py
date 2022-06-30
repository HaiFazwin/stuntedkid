import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Influenza Test

This app predicts the **Influenza Test** type!
""")

st.sidebar.header('How are you?')

def user_input_features():
    Temperature = st.sidebar.slider('Your Temperature', 35, 36, 37,38,39,40,41,42,43,44)
    Running Nose = st.sidebar.slider('Running Nose?', Yes, No)
    cough = st.sidebar.slider('Coughing?', Yes, No)
    Dizziness = st.sidebar.slider('Dizziness?', Yes, No)
    data = {'Temperature': Your Temperature,
            'Running Nose': Running Nose,
            'Cough': Coughing?,
            'Dizziness': Dizziness}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/HaiFazwin/stuntedkid/main/Untitled%20spreadsheet%20-%20Sheet1.csv')
X = iris.drop('Result',axis=1)
Y = iris.Result

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(['Positive','Negatif'])

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
