import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv("heart.csv")
    df = df[["age", "sex", "cp", "trestbps", "chol","fbs","restecg","thalach","thal","target"]]
    df = df.rename({"sex": "gender"}, axis=1)
    df = df.rename({"cp": "chest_pain"}, axis=1)
    df = df.rename({"trestbps": "blood_pressure"}, axis=1)
    df = df.rename({"chol": "cholestoral"}, axis=1)
    df = df.rename({"fbs": "blood_sugar"}, axis=1)
    df = df.rename({"restecg": "resting_electrocardiographic_results"}, axis=1)
    df = df.rename({"thalach": "maximum_heart_rate_achieved"}, axis=1)
    df = df.rename({"thal": "thalassemia"}, axis=1)
    df = df.rename({"target": "heart_disease"}, axis=1)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Heart Disease Prediction")

    st.write(
        """
    ### Kaggle Heart Disease CSV file
    """
    )
    
   # data = df["age"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Based Upon Age""")

    #st.pyplot(fig1)
    
    #st.write(
    #3    """
    #### Heart Disease Based On Age
    #"""
    #)

    #data = df.groupby(["age"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Heart Disease Based On Age
    #"""
    )

    data = df.groupby(["age"])["heart_disease"].mean().sort_values(ascending=True)
    st.line_chart(data)

###### heart disease based upon gender
    data = df["gender"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Heart Disease Based Upon Gender""")

    st.pyplot(fig1)
    
  

   

###### heart disease due to chest pain
    #data = df["chest_pain"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Based Upon Chest Pain""")

    #st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Based Due to Chest Pain
    #"""
    #)

    #data = df.groupby(["chest_pain"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    #st.write(
    #    """
    #### Mean Heart Disease Due to Chest Pain
    #"""
    #)

    #data = df.groupby(["chest_pain"])["heart_disease"].mean().sort_values(ascending=True)
    #st.line_chart(data)
###### heart disease due to blood pressure
    #data = df["blood_pressure"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Due to Blood Pressure""")

    #st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Due to Blood Pressure
    #"""
    #)

    #data = df.groupby(["blood_pressure"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Heart Disease Due to Blood Pressure
    #"""
    )

    data = df.groupby(["blood_pressure"])["heart_disease"].mean().sort_values(ascending=True)
    st.line_chart(data)
###### heart disease due to cholestrol
    #data = df["cholestoral"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Due to Cholestoral""")

    #st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Due to Cholestoral
    #"""
    #)

    #data = df.groupby(["cholestoral"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Heart Disease Due to cholestoral
    #"""
    )

    data = df.groupby(["cholestoral"])["heart_disease"].mean().sort_values(ascending=True)
    st.line_chart(data)
###### heart disease due to  blood sugar
    data = df["blood_sugar"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Heart Disease Due to Blood Sugar""")

    st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Due to Blood Sugar
    #"""
    #)

    #data = df.groupby(["blood_sugar"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    #st.write(
    #    """
    #### Mean Heart Disease Due to Blood Sugar
    #"""
    #)

    #data = df.groupby(["blood_sugar"])["heart_disease"].mean().sort_values(ascending=True)
    #st.line_chart(data)
###### heart disease based on electocardiographic results
    data = df["resting_electrocardiographic_results"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Heart Disease Based on Electrocardiographic Results""")

    st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Based on Electrocardiographic Results
    #"""
    #)

    #data = df.groupby(["resting_electrocardiographic_results"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    #st.write(
    #    """
    #### Mean Heart Disease Based on Electrocardiographic Results
    #"""
   # )

    #data = df.groupby(["resting_electrocardiographic_results"])["heart_disease"].mean().sort_values(ascending=True)
    #st.line_chart(data)
###### heart disease based on maximum heart rate acheived
    #data = df["maximum_heart_rate_achieved"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Based Upon Maximum Heart Rate Acheived""")

    #st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Based Upon Maximum Heart Rate Acheived
    #"""
    #)

    #data = df.groupby(["maximum_heart_rate_achieved"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Heart Disease Based Upon Maximum Heart Rate Acheived
    #"""
    )

    data = df.groupby(["maximum_heart_rate_achieved"])["heart_disease"].mean().sort_values(ascending=True)
    st.line_chart(data)
###### heart disease due to thalassemia
    #data = df["thalassemia"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    #st.write("""#### Heart Disease Based Upon Thalassemia""")

    #st.pyplot(fig1)
    
    #st.write(
    #    """
    #### Heart Disease Based Upon Thalassemia
    #"""
    #)

    #data = df.groupby(["thalassemia"])["heart_disease"].mean().sort_values(ascending=True)
    #st.bar_chart(data)

    st.write(
        """
    #### Mean Heart Disease Based Upon Thalassemia
    #"""
    )

    data = df.groupby(["thalassemia"])["heart_disease"].mean().sort_values(ascending=True)
    st.line_chart(data)