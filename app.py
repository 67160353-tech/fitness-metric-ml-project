import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# --- 1. ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="Fitness Predictor", layout="wide")

# --- 2. ฟังก์ชัน Train โมเดลสดๆ (แก้ปัญหาไฟล์ .pkl พัง) ---
@st.cache_resource
def train_model():
    # โหลดข้อมูลจาก GitHub (ชื่อไฟล์ต้องตรงกับใน Repo คุณ)
    df = pd.read_csv('exercise_dataset.csv')
    df = df.dropna()

    X = df.drop(columns=['ID', 'Calories Burn'])
    y = df['Calories Burn']

    numerical_features = ['Dream Weight', 'Actual Weight', 'Age', 'Duration', 'Heart Rate', 'BMI', 'Exercise Intensity']
    categorical_features = ['Exercise', 'Gender', 'Weather Conditions']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    model_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    model_pipeline.fit(X, y)
    return model_pipeline

# เรียกใช้งานฟังก์ชัน Train
with st.spinner('กำลังเตรียมระบบ ML... กรุณารอสักครู่'):
    model = train_model()

# --- 3. ส่วน UI (เหมือนเดิม) ---
st.title("🏃‍♂️ Exercise & Fitness Metrics Predictor")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    exercise = st.selectbox("ประเภทการออกกำลังกาย", ['Yoga', 'Running', 'Cardio', 'Strength'])
    gender = st.selectbox("เพศ", ['Male', 'Female'])
    age = st.number_input("อายุ", 10, 100, 25)
    duration = st.number_input("ระยะเวลา (นาที)", 1, 300, 30)
    intensity = st.slider("ระดับความเหนื่อย", 1, 10, 5)

with col2:
    actual_weight = st.number_input("น้ำหนักปัจจุบัน (kg)", 30.0, 200.0, 70.0)
    dream_weight = st.number_input("น้ำหนักเป้าหมาย (kg)", 30.0, 200.0, 65.0)
    heart_rate = st.number_input("อัตราการเต้นของหัวใจ (bpm)", 40, 220, 120)
    weather = st.selectbox("สภาพอากาศ", ['Sunny', 'Rainy', 'Cloudy'])

if st.button("🚀 คำนวณแคลอรี่"):
    # คำนวณ BMI เบื้องต้น
    bmi = actual_weight / ((1.7)**2) 
    
    input_df = pd.DataFrame([{
        'Exercise': exercise, 'Gender': gender, 'Age': age, 
        'Duration': duration, 'Actual Weight': actual_weight, 
        'Dream Weight': dream_weight, 'Heart Rate': heart_rate, 
        'Weather Conditions': weather, 'BMI': bmi, 
        'Exercise Intensity': intensity
    }])
    
    prediction = model.predict(input_df)
    st.success(f"### 🔥 ผลการทำนาย: {prediction[0]:.2f} kcal")
