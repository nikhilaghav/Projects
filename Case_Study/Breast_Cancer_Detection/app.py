import os
import streamlit as st
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.title("Breast Cancer Prediction")
st.write("Machine Learning application dashboard")

model_data = joblib.load(
    os.path.join(BASE_DIR, "BreastCancerVoting.pkl")
)

model = model_data["model"]
scaler = model_data["scaler"]
feature_names = model_data["feature_names"]

st.subheader("Enter Patient Details:")

patient_details = {}

for feature in feature_names:

    patient_details[feature] = st.number_input(
        feature,
        value=0.0,
        format="%.4f"
    )

if st.button("Predict"):

    new_patient = pd.DataFrame(
        [patient_details],
        columns=feature_names
    )

    new_patient_scaled = scaler.transform(new_patient)

    prediction = model.predict(new_patient_scaled)[0]

    if prediction == 1:
        st.success("Prediction : Class 1(Benign)")

    else:
        st.error("Prediction : Class 0(malignant)")

st.divider()
