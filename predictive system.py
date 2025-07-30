# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import pandas as pd

loaded_model = pickle.load(open('E:/ml_project/trained_model.sav', 'rb'))


new_car = {
    'Present_Price'       : 7.5,
    'Kms_Driven'          : 35_000,
    'Owner'               : 0,
    'Car_Age'             : 5,
    'Fuel_Type_Diesel'    : 1,
    'Fuel_Type_Petrol'    : 0,
    'Seller_Type_Individual': 1,
    'Transmission_Manual'   : 0
}

new_car_df = pd.DataFrame([new_car])
pred_price = loaded_model.predict(new_car_df)[0]
print(f"Predicted selling price: {pred_price:.2f} lakh ₹")