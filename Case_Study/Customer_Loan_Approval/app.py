import streamlit as st
import pandas as pd
import joblib

from pathlib import Path


# Step 1 : Page Configuration

st.set_page_config(
    page_title="Customer Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)


# Step 2 : Load Trained Model

BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "LoanApprovalModel.pkl"

if not model_path.exists():

    st.error("Model file not found. Please run model.py first.")

    st.stop()


model_data = joblib.load(model_path)

model = model_data["model"]

scaler = model_data["scaler"]

feature_names = model_data["features"]


# Step 3 : Application Title

st.title("🏦 Customer Loan Approval Prediction")

st.markdown(
    "### Machine Learning Application using Voting Classifier"
)

st.write(
    "Enter customer details to predict whether the loan will be approved."
)

st.divider()


# Step 4 : Customer Information

st.subheader("Customer Information")


age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100,
    value=30,
    step=1
)


income = st.number_input(
    "Customer Income",
    min_value=0,
    value=50000,
    step=1000
)


credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700,
    step=1
)


existing_loan = st.selectbox(
    "Existing Loan",
    options=["No", "Yes"]
)


employment_experience = st.number_input(
    "Employment Experience (Years)",
    min_value=0,
    max_value=60,
    value=5,
    step=1
)


loan_amount = st.number_input(
    "Requested Loan Amount",
    min_value=0,
    value=200000,
    step=10000
)


# Step 5 : Convert Categorical Input

if existing_loan == "Yes":

    existing_loan_value = 1

else:

    existing_loan_value = 0


# Step 6 : Prepare Input Data

input_data = pd.DataFrame(
    [[
        age,
        income,
        credit_score,
        existing_loan_value,
        employment_experience,
        loan_amount
    ]],
    columns=[
        "Age",
        "Income",
        "CreditScore",
        "ExistingLoan",
        "EmploymentExperience",
        "LoanAmount"
    ]
)


# Step 7 : Prediction

st.divider()

if st.button("Predict Loan Approval", type="primary"):

    # Arrange features in training order
    input_data = input_data[feature_names]

    # Apply feature scaling
    input_scaled = scaler.transform(input_data)

    # Predict loan approval
    prediction = model.predict(input_scaled)

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.success("Loan Approved")

        st.write(
            "The machine learning model predicts that the "
            "customer's loan application may be approved."
        )

    else:

        st.error("Loan Not Approved")

        st.write(
            "The machine learning model predicts that the "
            "customer's loan application may not be approved."
        )

    # Display prediction probability if available
    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(input_scaled)[0]

        approved_index = list(model.classes_).index(1)

        approval_probability = probability[approved_index] * 100

        st.write(
            f"Model Approval Probability: "
            f"{approval_probability:.2f}%"
        )


# Step 8 : Footer

st.divider()
