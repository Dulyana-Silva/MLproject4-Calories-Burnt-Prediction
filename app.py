import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('predictor.pkl')

st.title("Calories Burnt Prediction App")
st.write("Enter your details to predict the calories burnt during the workout.")

# Input field
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=25)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
duration = st.number_input("Workout Duration (minutes)", min_value=1, max_value=300, value=60)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=70)
body_temp = st.number_input("Body Temperature (°C)", min_value=30, max_value=45, value=37)

# Encode categorical to numerical
gender_value = 0 if gender == "Male" else 1

# Generating the Prediction
if st.button("Predict Calories Burnt"):
    input_data = np.array([[gender_value, age, height, weight, duration, heart_rate, body_temp]])

    prediction = model.predict(input_data)


st.success(f"Estimated Calories Burned: {prediction[0]:.2f}")  # 2f --> means show only 2 decimal places
st.write("This prediction is based on the trained ML model.")