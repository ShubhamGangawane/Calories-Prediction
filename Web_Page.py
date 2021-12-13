# Importing Libraries
from os import write
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

def Page():

    st.write("##### Hello everyone, This project is about calorie prediction with machine learning using python.")
    st.write("Calories in the foods we eat provide energy in the form of heat so that our bodies can function. This means that we need to eat a certain amount of calories just to sustain life. But if we take in too many calories, then we risk gaining weight.")
    st.write("So there is need to burn Calories, for burning calories we doing exercises and more. Now Lets Predict Some Calories.")

    st.write("")
    st.write("")
    st.write("")

    # BMI image
    bmi_image = Image.open('img_bmi.jpg')
    st.sidebar.image(bmi_image,"")


    # Calories image 
    cal_image = Image.open("img_calories.jpg")
    st.image(cal_image,"")

    # Reading Calories Prediction Saved Model
    saved_file = pickle.load(open("C:\\Users\\Anjali\\Documents\\Jupter\\1. Machine Learning\\15. Final Project\Code\\caloriesprediction.sav","rb"))

    # Heading first streamlit function
    st.sidebar.write("# BMI Calculator")
    st.sidebar.write("**Lets First Calculate your BMI**")

    
    st.write("")
    st.write("")
    st.write("")

    # BMI Calculator
    height = st.sidebar.slider("Select your height (in cm)",140,200,150)
    weight = st.sidebar.slider("Select your weight (in kg)",50,120,57)

    bmi = weight / ((height / 100)**2)
    bmi = round(bmi,2)


    # BMI DataFrame
    st.write("##### Body Mass Index")

    data = {
        "Height":height,
        "Weight":weight,
        "BMI":str(np.round(bmi,2))
        }

    bmi1 = pd.DataFrame(data,index=[0])
    bmi1 = round(bmi1,2)
    st.write(bmi1)


    # interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    elif(bmi >= 30):
        st.error("You are Extremely Overweight")


    # Calories Data
    st.sidebar.write("# Calories Data")


    Age = st.sidebar.slider('Age of a Person (20-80)',20,80,24)
    Duration = st.sidebar.slider("Duration of Workout",0,30,10)
    Heart_Rate = st.sidebar.slider("Heart Rate of a Person (70 - 120)",70,120,80)
    Body_Temp = float(st.sidebar.slider("Body Temperature of a Person (36 - 42)",36.0,42.0,40.3,step=0.1))
    BMI = st.sidebar.slider("Body Mass Index (18 - 30)",18.0,35.9,20.20,step=0.1)
    gender = st.sidebar.slider("Gender [1 Male & 0 Female]",0,1,1)


    # Calories Data DataFrame
    st.write('##### User Data')

    calories_data = {
        "Age":Age,
        "Duration":Duration,
        "Heart_Rate":Heart_Rate,
        "Body_Temp":str(np.round(Body_Temp,1)),
        "BMI":str(np.round(BMI,2)),
        "Gender":gender
        }

    calories_data = pd.DataFrame(calories_data,index=[1])
    st.write(calories_data)

    # interpretation of BMI index of user data
    if(BMI < 16):
        st.error("You are Extremely Underweight")
    elif(BMI >= 16 and BMI < 18.5):
        st.warning("You are Underweight")
    elif(BMI >= 18.5 and BMI < 25):
        st.success("You are Healthy")       
    elif(BMI >= 25 and BMI < 30):
        st.warning("You are Overweight")
    elif(BMI >= 30):
        st.error("You are Extremely Overweight")


    st.write('')
    st.write("")
    st.write("")
    st.write("") 
    st.write("") 

    # Calories Prediction DataFrame
    st.write("##### Prediction")

    predicted = saved_file.predict([[Age,Duration,Heart_Rate,Body_Temp,BMI,gender]])

    predicted = {
        "You Haved Burned":str(np.round(predicted[0],1)) + "  Calories"
    }

    df_predicted = pd.DataFrame(predicted,index=[2])

    st.write(df_predicted)

    st.success("**Keep Doing Exercises !!!**")



