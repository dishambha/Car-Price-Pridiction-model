# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 00:54:57 2025

@author: Dishambha Awasthi
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

# --- LOAD THE SAVED MODEL ---
# Note: Ensure 'trained_model.sav' is in the correct path.
# Using a relative path is often better for deployment.
try:
    loaded_model = pickle.load(open('E:/ml_project/trained_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'trained_model.sav' is in the correct directory.")
    st.stop()


# --- THE PREDICTION FUNCTION ---
def car_price_prediction():
    """
    This function contains the Streamlit web interface and the prediction logic.
    """

    # --- PAGE CONFIGURATION & TITLE ---
    st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")
    st.title("🚗 Car Price Prediction")
    st.write("Enter the details of the car to predict its selling price.")
    st.markdown("---")


    # --- USER INPUTS IN COLUMNS FOR A BETTER LAYOUT ---
    col1, col2 = st.columns(2)

    with col1:
        present_price = st.number_input('**Present Price (in Lakhs ₹)**', min_value=0.1, value=7.5, step=0.1, format="%.2f")
        kms_driven = st.number_input('**Kilometers Driven**', min_value=0, value=35000, step=1000)
        fuel_type = st.selectbox('**Fuel Type**', ['Petrol', 'Diesel', 'CNG'])
        seller_type = st.selectbox('**Seller Type**', ['Dealer', 'Individual'])

    with col2:
        car_age = st.number_input('**Car Age (in years)**', min_value=0, max_value=20, value=5, step=1)
        owner = st.selectbox('**Number of Previous Owners**', [0, 1, 2, 3])
        transmission = st.selectbox('**Transmission Type**', ['Manual', 'Automatic'])

    st.markdown("---")


    # --- PREDICTION LOGIC ---
    prediction_result = ''

    # Create a button to trigger the prediction
    if st.button('**Predict Selling Price**', key='predict_button'):
        # 1. Preprocess categorical inputs into the model's expected format
        fuel_type_petrol = 1 if fuel_type == 'Petrol' else 0
        fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
        # (If fuel_type is 'CNG', both petrol and diesel will be 0)

        seller_type_individual = 1 if seller_type == 'Individual' else 0
        # (If seller_type is 'Dealer', individual will be 0)

        transmission_manual = 1 if transmission == 'Manual' else 0
        # (If transmission is 'Automatic', manual will be 0)


        # 2. Create a DataFrame with the exact column names the model was trained on
        input_data = pd.DataFrame(
            [[
                present_price,
                kms_driven,
                owner,
                car_age,
                fuel_type_diesel,
                fuel_type_petrol,
                seller_type_individual,
                transmission_manual
            ]],
            columns=[
                'Present_Price',
                'Kms_Driven',
                'Owner',
                'Car_Age',
                'Fuel_Type_Diesel',
                'Fuel_Type_Petrol',
                'Seller_Type_Individual',
                'Transmission_Manual'
            ]
        )

        # 3. Make the prediction
        car_prediction = loaded_model.predict(input_data)

        # 4. Format the result
        prediction_result = f"The predicted selling price is **{car_prediction[0]:.2f} Lakh ₹**"


    # Display the prediction result if it exists
    if prediction_result:
        st.success(prediction_result)


# --- RUN THE APP ---
if __name__ == '__main__':
    car_price_prediction()