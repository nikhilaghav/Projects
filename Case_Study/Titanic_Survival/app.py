import os
import streamlit as st
import pandas as pd
import joblib 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.title("Titanic survival case study")
st.write("Machine Learning application dashboad")

model = joblib.load(os.path.join(BASE_DIR, "MarvellousTitanic.pkl"))

st.subheader("Enter Passenger details:")

age = st.number_input("age",min_value=0)
fare = st.number_input("fare",min_value=0)
sex= st.number_input("sex(0-male/1-female)",min_value=0)
sibsp= st.number_input("No. of siblings and spouses",min_value=0)
parch= st.number_input("No. of parents and child",min_value=0)
pclass= st.number_input("passenger class(1/2/3)",min_value=0)
embarked= st.number_input("embarked(0-Cherbourg/1-Queenstown/2-Southampton)",min_value=0)

if st.button("Predict "):
    new_passenger = pd.DataFrame({
    "Age":[age],
    "Fare":[fare],
    "Sex":[sex],
    "sibsp":[sibsp],
    "Parch":[parch],
    "Pclass":[pclass],
    "Embarked":[embarked]
    })

    prediction = model.predict(new_passenger)[0]

    if prediction == 1:
        st.success("passenger survived")

    else:
        st.error("passenger did not survived")

st.divider()
