import streamlit as st
import pandas as pd
import joblib

from pathlib import Path


########################################
# Step 1 : Page Configuration
########################################

st.set_page_config(
    page_title="Wine Classification System",
    page_icon="🍷",
    layout="wide"
)


########################################
# Step 2 : Load Trained Model
########################################

BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "WinePredictor.pkl"

if not model_path.exists():

    st.error("Model file not found. Please run model.py first.")

    st.stop()


model_data = joblib.load(model_path)

model = model_data["model"]

scaler = model_data["scaler"]

feature_names = model_data["features"]


########################################
# Step 3 : Application Title
########################################

st.title("🍷 Wine Classification System")

st.markdown(
    "### Machine Learning Application using K-Nearest Neighbors"
)

st.write(
    "Enter the chemical characteristics of a wine "
    "to predict its classification."
)

st.divider()


########################################
# Step 4 : Wine Characteristics
########################################

st.subheader("Wine Chemical Properties")

col1, col2 = st.columns(2)


with col1:

    alcohol = st.number_input(
        "Alcohol",
        min_value=0.0,
        value=13.0,
        step=0.1
    )

    malic_acid = st.number_input(
        "Malic Acid",
        min_value=0.0,
        value=2.0,
        step=0.1
    )

    ash = st.number_input(
        "Ash",
        min_value=0.0,
        value=2.3,
        step=0.1
    )

    alcalinity = st.number_input(
        "Alcalinity of Ash",
        min_value=0.0,
        value=19.0,
        step=0.1
    )

    magnesium = st.number_input(
        "Magnesium",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_phenols = st.number_input(
        "Total Phenols",
        min_value=0.0,
        value=2.3,
        step=0.1
    )

    flavanoids = st.number_input(
        "Flavanoids",
        min_value=0.0,
        value=2.0,
        step=0.1
    )


with col2:

    nonflavanoid_phenols = st.number_input(
        "Nonflavanoid Phenols",
        min_value=0.0,
        value=0.3,
        step=0.01
    )

    proanthocyanins = st.number_input(
        "Proanthocyanins",
        min_value=0.0,
        value=1.5,
        step=0.1
    )

    color_intensity = st.number_input(
        "Color Intensity",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    hue = st.number_input(
        "Hue",
        min_value=0.0,
        value=1.0,
        step=0.01
    )

    od280 = st.number_input(
        "OD280/OD315 of Diluted Wines",
        min_value=0.0,
        value=2.5,
        step=0.1
    )

    proline = st.number_input(
        "Proline",
        min_value=0.0,
        value=750.0,
        step=10.0
    )


########################################
# Step 5 : Prepare Input Data
########################################

input_data = pd.DataFrame(
    [[
        alcohol,
        malic_acid,
        ash,
        alcalinity,
        magnesium,
        total_phenols,
        flavanoids,
        nonflavanoid_phenols,
        proanthocyanins,
        color_intensity,
        hue,
        od280,
        proline
    ]],
    columns=[
        "Alcohol",
        "Malic acid",
        "Ash",
        "Alcalinity of ash",
        "Magnesium",
        "Total phenols",
        "Flavanoids",
        "Nonflavanoid phenols",
        "Proanthocyanins",
        "Color intensity",
        "Hue",
        "OD280/OD315 of diluted wines",
        "Proline"
    ]
)


########################################
# Step 6 : Prediction
########################################

st.divider()

if st.button("Predict Wine Class", type="primary"):

    # Arrange features in training order
    input_data = input_data[feature_names]

    # Apply feature scaling
    input_scaled = scaler.transform(input_data)

    # Predict wine class
    prediction = model.predict(input_scaled)

    predicted_class = prediction[0]

    st.subheader("Prediction Result")

    st.success(
        f"Predicted Wine Class : {predicted_class}"
    )

    # Calculate prediction probabilities
    probabilities = model.predict_proba(input_scaled)[0]

    st.subheader("Class Probabilities")

    for wine_class, probability in zip(
        model.classes_,
        probabilities
    ):

        st.write(
            f"Class {wine_class} : {probability * 100:.2f}%"
        )

        st.progress(float(probability))


########################################
# Step 7 : Display Input Data
########################################

    st.subheader("Entered Wine Characteristics")

    st.dataframe(input_data)


########################################
# Step 8 : Footer
########################################

st.divider()
