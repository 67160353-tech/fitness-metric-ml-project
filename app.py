import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fitness_model.pkl')

st.title("🏃‍♂️ Exercise & Fitness Metrics Predictor")
st.write("กรอกข้อมูลการออกกำลังกายของคุณเพื่อทำนายผล")

col1, col2 = st.columns(2)

with col1:
    exercise = st.selectbox("ประเภทการออกกำลังกาย", ['Yoga', 'Running', 'Cardio', 'Strength'])
    gender = st.selectbox("เพศ", ['Male', 'Female'])
    age = st.number_input("อายุ", min_value=1, max_value=100, value=25)
    duration = st.number_input("ระยะเวลา (นาที)", min_value=1, value=30)

with col2:
    actual_weight = st.number_input("น้ำหนักปัจจุบัน (kg)", min_value=1, value=70)
    dream_weight = st.number_input("น้ำหนักเป้าหมาย (kg)", min_value=1, value=65)
    heart_rate = st.number_input("อัตราการเต้นของหัวใจ (bpm)", min_value=40, value=120)
    weather = st.selectbox("สภาพอากาศ", ['Sunny', 'Rainy', 'Cloudy'])

input_df = pd.DataFrame([{
    'Exercise': exercise,
    'Gender': gender,
    'Age': age,
    'Duration': duration,
    'Actual Weight': actual_weight,
    'Dream Weight': dream_weight,
    'Heart Rate': heart_rate,
    'Weather Conditions': weather,
    'BMI': actual_weight / ((1.7)**2), # ตย. สูตร BMI (ความสูงสมมติ 1.7m)
    'Exercise Intensity': 5 # ค่าสมมติเบื้องต้น
}])

if st.button("ทำนายผลแคลอรี่"):
    prediction = model.predict(input_df)
    st.success(f"🔥 ปริมาณแคลอรี่ที่เผาผลาญประมาณ: {prediction[0]:.2f} kcal")
    
    st.info("Tip: การรักษา Heart Rate ให้อยู่ในโซนที่เหมาะสมจะช่วยเผาผลาญได้ดีขึ้น!")
