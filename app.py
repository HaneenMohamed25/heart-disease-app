import pickle 
import streamlit as st
import pandas as pd

# Load the model
model = pickle.load(open(r'D:\Heart_Failure_Prediction_model.sav','rb'))

# UI Title and Info
st.title("💓 Heart Disease Prediction Web App")
st.info("This app allows you to enter patient details to predict the risk of heart failure.")
st.sidebar.header('🧬 Patient Information')

# Sidebar Inputs
age = st.sidebar.slider("Age", 18, 100, step=1)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
chest_pain = st.sidebar.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])
resting_bp = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 0, 200, step=1)
cholesterol = st.sidebar.slider("Cholesterol (mg/dl)", 0, 603, step=1)
fasting_bs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
resting_ecg = st.sidebar.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.sidebar.slider("Max Heart Rate Achieved", 60, 202, step=1)
exercise_angina = st.sidebar.selectbox("Exercise-Induced Angina", ["Yes", "No"])
oldpeak = st.sidebar.number_input("Oldpeak (ST depression)", 0.0, 6.5, step=0.1)
st_slope = st.sidebar.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Manual One-Hot Encoding
data = {
    'Age': age,
    'Sex': 1 if sex == "Male" else 0,
    'RestingBP': resting_bp,
    'Cholesterol': cholesterol,
    'FastingBS': 1 if fasting_bs == "Yes" else 0,
    'MaxHR': max_hr,
    'ExerciseAngina': 1 if exercise_angina == "Yes" else 0,
    'Oldpeak': oldpeak,

    # One-hot: Chest Pain (drop first → ASY dropped)
    'ChestPainType_ATA': 1 if chest_pain == "ATA" else 0,
    'ChestPainType_NAP': 1 if chest_pain == "NAP" else 0,
    'ChestPainType_TA': 1 if chest_pain == "TA" else 0,

    # One-hot: RestingECG (drop first → LVH dropped)
    'RestingECG_Normal': 1 if resting_ecg == "Normal" else 0,
    'RestingECG_ST': 1 if resting_ecg == "ST" else 0,

    # One-hot: ST Slope (drop first → Down dropped)
    'ST_Slope_Flat': 1 if st_slope == "Flat" else 0,
    'ST_Slope_Up': 1 if st_slope == "Up" else 0
}

# Convert to DataFrame
df = pd.DataFrame([data])

# Prediction
if st.button("🔍 Predict"):
    result = model.predict(df)[0]
    st.subheader("🧾 Prediction Result:")
    if result == 1:
        st.error("⚠️ High Risk: The patient is likely to have heart disease.")
    else:
        st.success("✅ Low Risk: The patient is not likely to have heart disease.")






    