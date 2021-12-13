import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

@st.cache
def data():
    # Loading the data from csv file to pandas data frame
    # Loading the calories file.
    target = pd.read_csv("C:\\Users\\Anjali\\Documents\\Jupter\\1. Machine Learning\\15. Final Project\\calories.csv")
    target.shape

    # Loading the exercises file
    features = pd.read_csv("C:\\Users\\Anjali\\Documents\\Jupter\\1. Machine Learning\\15. Final Project\\exercise.csv")
    features.shape

    # Now Merging or concatening the files
    calories = pd.concat([features,target["Calories"]],axis=1)
    calories.shape

    # Droping the User_id column.
    calories.drop("User_ID",axis=1,inplace=True)

    # Calculating the BMI
    calories["BMI"] = calories["Weight"] / ((calories["Height"] / 100)**2)
    calories["BMI"] = round(calories["BMI"] , 1)

    # BMI numeric to bmi_category for better understanding of the data
    bmi_category = ["UnderWeight" , "Normal" , "OverWeight" , "Obsese"] 
    calories["bmi_category"] = pd.cut(calories["BMI"] , bins = [0 , 18  , 25 , 30 , 35 ] , right=False , labels=bmi_category)
    calories["bmi_category"].head()

    # we have to split this age data into categorical age_groups to fnd which age_groups are higher in this dataset and there bmi scores . 
    age_groups = ["Young", "Middle" , "Old"]
    calories["age_groups"] = pd.cut(calories["Age"] , bins= [20,40,60,80] , right=False , labels= age_groups)
    
    return calories

# Saving the function data into df
df = data()


# Making a function for uploading Calories visualization graphs into streamlit.

def visualization():

    st.write("## **Calories Visualization Graphs**")

    # 1. Heart_Rate v Calories
    st.write("##### **Heart Rate v  Calories**")

    heart_rate_calories = df.groupby(["Heart_Rate"])["Calories"].mean().sort_values(ascending=True)
    st.line_chart(heart_rate_calories)
    st.write("- **Heart Rate** increases the **calories** are burning faster because at that time of workout we even sweat too much")


    # 2. Duration v Calories
    st.write("##### **Duration v Calories**")

    calories_duration = df.groupby(["Duration"])["Calories"].mean().sort_values(ascending=True)
    st.line_chart(calories_duration)
    st.write("- As the **duration** of workout increases the **calories** is burning **higher** in **males** body")


    # 3. Body Temperature v Calories
    st.write("##### **Body Temperature v Calories**")

    body_temp_calories = df.groupby(["Body_Temp"])["Calories"].mean().sort_values(ascending=True)
    st.line_chart(body_temp_calories)
    st.write('- **Male** and **Female** both body_temp are higest at **41C**')

    
    # 4. Age_Group v Calories
    st.write("##### **Age_Group v Calories**")

    age_calories = df.groupby(["age_groups"])["Calories"].mean().sort_values(ascending=True)
    st.bar_chart(age_calories)

    st.write("- **Old** people tend to burn more **calories**")


    # 5. bmi_category v calories
    st.write("##### **BMI Category v Calories**")

    age_bmi_category = df.groupby(["bmi_category"])["Calories"].mean().sort_values(ascending=True)
    st.bar_chart(age_bmi_category)

    st.write("- **Overweights** are Burning more **Calories** as expected")


    # 7. Plotting  age_groups pie chart for better understanding of age percentages.

    st.write("##### **Age Groups**")

    fig , ax = plt.subplots()
    ax.pie(df["age_groups"].value_counts(),
    autopct="%.1f%%",
    shadow=True,
    explode=(0,0,0.1),
    labels=["Young","Middle","Old"],
    radius=1)

    ax.axis("equal")
    st.pyplot(fig)
    st.write("- We have found out that Young People are highly interested in burning calories.")
    


    # 8. Plotting Gender pie chart

    st.write("##### **Gender**")

    fig1, ax = plt.subplots()
    ax.pie(df["Gender"].value_counts(),
    autopct="%.1f%%",
    shadow=True,
    labels=["Male","Female"],
    radius=0.2,
    colors=['c',"pink"])

    ax.axis("equal")
    st.pyplot(fig1)
    st.write("- We have equal distibution of **Male** and **Female** data points ")
