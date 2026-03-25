# 🏃‍♂️ Exercise & Fitness Metrics Predictor

## 📌 Problem Statement (นิยามปัญหา)
โปรเจคนี้จัดทำขึ้นเพื่อช่วยให้ผู้ที่ออกกำลังกายสามารถคาดการณ์ผลลัพธ์ (เช่น แคลอรี่ที่เผาผลาญ หรือ ระดับความเหนื่อย) 
จากปัจจัยต่างๆ เช่น อัตราการเต้นของหัวใจ, ระยะเวลา และประเภทการออกกำลังกาย 
เพื่อช่วยในการวางแผนการออกกำลังกายให้มีประสิทธิภาพมากขึ้น

## 📊 Dataset (ที่มาของข้อมูล)
- *Source:* [Exercise and Fitness Metrics Dataset (Kaggle)] (https://www.kaggle.com/datasets/aakashjoshi123/exercise-and-fitness-metrics-dataset))
- *Features:* ประกอบด้วยข้อมูลส่วนตัว (Age, Gender, BMI) และข้อมูลการออกกำลังกาย (Heart_Rate, Duration, Exercise_Type)
- *Target:* ทำนาย Calories_Burned (Regression) หรือ Intensity_Level (Classification)

## 🛠️ Technology Stack
- *Language:* Python
- *Libraries:* Pandas, Scikit-learn, Matplotlib, Seaborn
- *Deployment:* Streamlit

## App
Link:https://fitness-metric-ml-project-jfq2c8qrad3ggwbkjzvwf2.streamlit.app/

## Model
--- Model Accuracy Results ---
R-squared (R2 Score): -0.0422
Mean Absolute Error (MAE): 101.18 Calories
Root Mean Squared Error (RMSE): 117.41 Calories

จากการทดลองพบว่าฟีเจอร์ในชุดข้อมูลนี้มีค่า Correlation กับ Calories Burn ต่ำมาก (เกือบเป็น 0) ทำให้โมเดลแบบ Linear หรือ Random Forest ทั่วไปทำนายได้ยาก
หากต้องการเพิ่มความแม่นยำ ในอนาคตควรเก็บข้อมูลที่สัมพันธ์โดยตรงมากขึ้น เช่น ความเร็ว (Speed) หรือ ความลาดชัน (Incline) ขณะออกกำลังกาย
