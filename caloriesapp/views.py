from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import signUpForm, loginForm, postForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
import pickle
import pandas as pd
import numpy as np
import json


saved_file = pickle.load(open("G:\\Django\\MLdeploy\\savedmodels\\caloriesprediction.sav","rb"))

# Create your views here.

def home(request):
    return render(request, "blog/Home.html")


def about(request):
    return render(request, "blog/About.html")

def contact(request):
    return render(request, "blog/Contacts.html")


def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            height = request.POST["height"]
            weight = request.POST["weight"]
            height_m = float(height)
            weight = int(weight)

            height_m = height_m * 0.3048
            bmi = weight / (height_m ** 2)
            bmi = round(bmi,2)

            Age = request.POST["age"]
            Duration = request.POST["duration"]
            Heart_Rate = request.POST["heartRate"]
            Body_Temp = request.POST["bodyTemp"]
            Genders = request.POST["gender"]
            if Genders == "Male":
                gender = 1
            elif Genders == "Female":
                gender = 0
            else:
                gender = -1

            data = {
                "Height":height,
                "Weight":weight,
                "Age":Age,
                "Duration":Duration,
                "Heart":Heart_Rate,
                "Body":Body_Temp,
                "Gender":Genders,
            }
            bmi1 = pd.DataFrame(data, index=[0])
            json_records = bmi1.reset_index().to_json(orient ='records') 
            userData = json.loads(json_records)

            # interpretation of BMI index of user data
            if(bmi < 16):
                bmiResult = "Extremely Underweight"
            elif(bmi >= 16 and bmi < 18.5):
                bmiResult = "Underweight"
            elif(bmi >= 18.5 and bmi < 25): 
                bmiResult = "Healthy"       
            elif(bmi >= 25 and bmi < 30):
                bmiResult = "Overweight"
            elif(bmi >= 30):
                bmiResult = "Extremely Overweight"


            predicted = saved_file.predict([[Age,Duration,Heart_Rate,Body_Temp,bmi,gender]])
            df_predicted = pd.DataFrame(predicted,index=[0])
            json_records1 = df_predicted.reset_index().to_json(orient ='records') 
            data2 = json.loads(json_records1)
            Prediction = data2[0]['0']
            return render(request, "blog/Home.html", {"data":userData, "bmi_result":bmiResult, "predict":Prediction, "username":request.user})
        
        else:
            print("GET")
        return render(request,"blog/Calories.html")
    else:
        return redirect("login")



def userLogout(request):
    logout(request)
    return redirect("home")

def userSignup(request):
    
    if request.method == "POST":
        form = signUpForm(request.POST)

        if form.is_valid():
            messages.success(request, "Congratulations!! You have Become an Author....")
            form.save()
    else:
        form = signUpForm()
    return render(request, "blog/Signup.html", {"forms":form})

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm(request=request, data=request.POST)

            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=name, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully!!......")
                    return redirect("dashboard")
        else:
            form = loginForm()
        return render(request, "blog/Login.html", {"forms":form})   
    
    else:
        return redirect("dashboard")
    

def addPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = postForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data["title"]
                desc = form.cleaned_data["desc"]

                pst = Post(title=title, desc=desc)
                pst.save()

                form = postForm()

        else:
            form = postForm()
        return render(request, "blog/AddPost.html", {"forms":form})

    else:
        return redirect("login")
    

def updatePost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk = id)
            form = postForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
        else:
            post = Post.objects.get(pk=id)
            form = postForm(instance=post)
        return render(request, "blog/UpdatePost.html", {"forms":form})
    else:
        return redirect("login")
    

def deletePost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk=id)
            post.delete()
            return redirect("dashboard")
    else:
        return redirect("login")