import streamlit as st
import pandas as pd
import joblib


# Step 1 : Configure Dashboard

st.set_page_config(
    page_title="California Housing Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Step 2 : Dashboard Title

st.title("California Housing Price Prediction")

st.header("Machine Learning Application")

st.write("Predict California housing prices using Bagging Regressor")


# Step 3 : Load Preserved Model

model = joblib.load("CaliforniaHousing.pkl")


# Step 4 : Accept User Input

st.subheader("Enter Housing Details")

MedInc = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.0
)

HouseAge = st.number_input(
    "House Age",
    min_value=0.0,
    value=20.0
)

AveRooms = st.number_input(
    "Average Rooms",
    min_value=0.0,
    value=5.0
)

AveBedrms = st.number_input(
    "Average Bedrooms",
    min_value=0.0,
    value=1.0
)

Population = st.number_input(
    "Population",
    min_value=0.0,
    value=1000.0
)

AveOccup = st.number_input(
    "Average Occupancy",
    min_value=0.0,
    value=3.0
)

Latitude = st.number_input(
    "Latitude",
    value=34.0
)

Longitude = st.number_input(
    "Longitude",
    value=-118.0
)


# Step 5 : Predict Housing Price

if st.button("Predict Housing Price"):

    new_house = pd.DataFrame({

        "MedInc": [MedInc],
        "HouseAge": [HouseAge],
        "AveRooms": [AveRooms],
        "AveBedrms": [AveBedrms],
        "Population": [Population],
        "AveOccup": [AveOccup],
        "Latitude": [Latitude],
        "Longitude": [Longitude]

    })

    # Ensure features follow the training order
    new_house = new_house[model.feature_names_in_]

    prediction = model.predict(new_house)[0]

    st.success("Prediction completed successfully!")

    st.subheader("Predicted Median House Value")

    st.metric(
        label="Estimated Housing Price",
        value=f"${prediction * 100000:,.2f}"
    )


# Step 6 : Footer

st.divider()

st.caption("California Housing Price Prediction | Machine Learning Project")
