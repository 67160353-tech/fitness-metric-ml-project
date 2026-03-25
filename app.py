import streamlit as st
import pandas as pd
import joblib
import os

# --- 1. การตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="Fitness Predictor", layout="wide")

# --- 2. ฟังก์ชันโหลดโมเดล (ป้องกัน Error) ---
@st.cache_resource
def load_model():
    model_path = 'fitness_model.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error("❌ ไม่พบไฟล์โมเดล (fitness_model.pkl) ใน GitHub ของคุณ")
        return None

model = load_model()

# --- 3. ส่วนหัวของแอป ---
st.title("🏃‍♂️ Exercise & Fitness Metrics Predictor")
st.markdown("### ทำนายปริมาณแคลอรี่ที่เผาผลาญจากการออกกำลังกาย")
st.write("---")

if model:
    # --- 4. ส่วนรับข้อมูล (Input) แบ่งเป็น 2 คอลัมน์เพื่อให้ดูง่าย ---
    col1, col2 = st.columns(2)

    with col1:
        st.header("👤 ข้อมูลส่วนตัว")
        gender = st.selectbox("เพศ (Gender)", ['Male', 'Female'])
        age = st.slider("อายุ (Age)", 10, 100, 25)
        actual_weight = st.number_input("น้ำหนักปัจจุบัน (kg)", 30.0, 200.0, 70.0)
        dream_weight = st.number_input("น้ำหนักเป้าหมาย (kg)", 30.0, 200.0, 65.0)

    with col2:
        st.header("🏋️ ข้อมูลการออกกำลังกาย")
        exercise = st.selectbox("ประเภทการออกกำลังกาย", ['Yoga', 'Running', 'Cardio', 'Strength'])
        duration = st.number_input("ระยะเวลา (นาที)", 1, 300, 30)
        heart_rate = st.number_input("อัตราการเต้นของหัวใจ (bpm)", 40, 220, 120)
        weather = st.selectbox("สภาพอากาศ", ['Sunny', 'Rainy', 'Cloudy'])
        intensity = st.slider("ระดับความเหนื่อย (1-10)", 1, 10, 5)

    # --- 5. การประมวลผล ---
    # คำนวณ BMI เพิ่มเติมตามที่คุณใช้ใน Pipeline
    bmi = actual_weight / ((1.7)**2) # สมมติความสูง 1.70 m

    # สร้าง DataFrame ให้ตรงกับตอนที่ Train (ชื่อ Column ต้องเป๊ะ!)
    input_data = pd.DataFrame([{
        'Exercise': exercise,
        'Gender': gender,
        'Age': age,
        'Duration': duration,
        'Actual Weight': actual_weight,
        'Dream Weight': dream_weight,
        'Heart Rate': heart_rate,
        'BMI': bmi,
        'Weather Conditions': weather,
        'Exercise Intensity': intensity
    }])

    st.write("---")
    
    # --- 6. ปุ่มทำนายผล ---
    if st.button("🚀 คำนวณแคลอรี่ที่เผาผลาญ"):
        try:
            prediction = model.predict(input_data)[0]
            
            # แสดงผลลัพธ์แบบสวยงาม
            st.balloons()
            st.success(f"### 🔥 คุณเผาผลาญไปได้ประมาณ: **{prediction:.2f} kcal**")
            
            # ส่วนแสดงคำแนะนำ (Bonus Content)
            st.info(f"💡 สำหรับการออกกำลังกายแบบ {exercise} นาน {duration} นาที ถือเป็นผลลัพธ์ที่ยอดเยี่ยม!")
            
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการทำนาย: {e}")
            st.warning("ตรวจสอบว่าชื่อ Column ในแอปตรงกับที่ใช้ Train ใน Colab หรือไม่")

# --- 7. ส่วนท้าย (Footer) ---
st.write("---")
st.caption("พัฒนาโดย: [Pannawit Kingmanee] | โปรเจค ML Deployment (DADS)")
