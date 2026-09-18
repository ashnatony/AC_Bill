import streamlit as st
import joblib

model_data = joblib.load("electric_bill_model.pkl")

model = model_data["model"]
poly = model_data["poly"]

st.title("Electric Bill Predictor")

ac_units = st.number_input(
    "Enter AC Units",
    min_value=10.0,
    step=1.0
)

if st.button("Predict"):

    if ac_units<=10 or ac_units>150:
        st.error("Input value out of range")
    else:
    
        data = [[ac_units]]
        data_poly = poly.transform(data)

        prediction = model.predict(data_poly)

        st.success(f"Expected Electric Bill: {prediction[0]:.2f}")
