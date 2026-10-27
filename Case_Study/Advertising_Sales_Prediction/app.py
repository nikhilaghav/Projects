import streamlit as st
import pandas as pd
import joblib

from pathlib import Path


# Step 1 : Page Configuration

st.set_page_config(
    page_title="Advertising Sales Prediction",
    page_icon="📊",
    layout="centered"
)


# Step 2 : Load Trained Model

BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "AdvertisingSales.pkl"

if not model_path.exists():

    st.error("Model file not found. Please run model.py first.")

    st.stop()


model = joblib.load(model_path)


# Step 3 : Application Title

st.title("📊 Advertising Sales Prediction")

st.markdown(
    "### Machine Learning Application using Linear Regression"
)

st.write(
    "Predict product sales based on advertising expenditure "
    "across different marketing channels."
)

st.divider()


# Step 4 : Advertising Information

st.subheader("Advertising Expenditure")


tv = st.number_input(
    "TV Advertising Budget",
    min_value=0.0,
    max_value=500.0,
    value=150.0,
    step=1.0
)


radio = st.number_input(
    "Radio Advertising Budget",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    step=1.0
)


newspaper = st.number_input(
    "Newspaper Advertising Budget",
    min_value=0.0,
    max_value=150.0,
    value=30.0,
    step=1.0
)


# Step 5 : Prepare Input Data

input_data = pd.DataFrame(
    [[tv, radio, newspaper]],
    columns=["TV", "radio", "newspaper"]
)


# Step 6 : Prediction

st.divider()

if st.button("Predict Sales", type="primary"):

    prediction = model.predict(input_data)

    predicted_sales = prediction[0]

    st.subheader("Prediction Result")

    st.success(
        f"Predicted Sales : {predicted_sales:.2f}"
    )

    st.info(
        "The predicted sales value is expressed in "
        "thousands of units."
    )


# Step 7 : Footer

st.divider()

