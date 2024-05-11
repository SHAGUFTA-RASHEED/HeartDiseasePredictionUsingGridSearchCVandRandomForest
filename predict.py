import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
age = data["age"]
gender = data["gender"]
chest_pain = data["chest_pain"]
blood_pressure = data["blood_pressure"]
cholestoral = data["cholestoral"]
blood_sugar = data["blood_sugar"]
resting_electrocardiographic_results = data["resting_electrocardiographic_results"]
maximum_heart_rate_achieved = data["maximum_heart_rate_achieved"]
thalassemia = data["thalassemia"]
def show_predict_page():
    st.title("Heart Disease Prediction")

    st.write("""### We need some information to predict the heart disease""")
    
    age= st.slider("Age", 0, 150, 20)
    gender = (
        "0",
        "1",   
    )
    gender = st.selectbox("Gender", gender)
    chest_pain = (
        "0","1","2","3",
    )

    chest_pain = st.selectbox("Chest Pain", chest_pain)
    blood_pressure = st.slider("Blood Pressure", 0, 200, 80)
    cholestoral = st.slider("Cholestrol", 0, 500, 80)
    blood_sugar=("0","1")
    blood_sugar = st.selectbox("Blood Sugar", blood_sugar)
    resting_electrocardiographic_results=("0", "1","2 ")
    resting_electrocardiographic_results= st.selectbox("ECG Results", resting_electrocardiographic_results)
    maximum_heart_rate_achieved = st.slider("Maximum Heart Rate Achieved", 80, 200, 90)
    thalassemia=("0","1","2")
    thalassemia= st.selectbox("Thalassemia", thalassemia)
    
    ok = st.button("Predict Heart Disease")
    if ok:
        X = np.array([[age,gender,chest_pain,blood_pressure,cholestoral,blood_sugar,resting_electrocardiographic_results,maximum_heart_rate_achieved,thalassemia ]])
        
        X = X.astype(float)
        

        heart_disease = regressor.predict(X)
        heart_disease=heart_disease[0]*100
        st.subheader(f"The chances of heart disease is {heart_disease}%")