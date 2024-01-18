from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Post

class signUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"should contain lowercase, uppercase, number and at least 6 characters..."}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {"first_name":"First Name", "last_name" : "Last Name", "email":"Email"}
        widgets = {"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username..."}),
                   "first_name":forms.TextInput(attrs={"class":"form-control"}),
                   "last_name":forms.TextInput(attrs={"class":"form-control"}),
                   "email":forms.TextInput(attrs={"class":"form-control","placeholder":"should contains '@' '.com' "})} 
        
    

class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus":True, "class":"form-control"}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete":"current-password", "class":"form-control"}))


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        widgets = {"title":forms.TextInput(attrs={"class":"form-control"}),
                   "desc":forms.Textarea(attrs={"class":"form-control"})}
