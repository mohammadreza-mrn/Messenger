

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate


UserModel = get_user_model()

class AuthForm(forms.Form):

    username = forms.CharField(max_length=150,error_messages={
        "required" : "Please Enter UserName",
        "null" : "Please Enter UserName",
        "blank" : "Please Enter UserName",
    })

    email = forms.CharField(max_length=150,error_messages={
        "required" : "Please Enter Email",
        "null" : "Please Enter Email",
        "blank" : "Please Enter Email",
    })

class RegisterForm(AuthForm):

    password = forms.CharField(max_length=150,min_length=8,error_messages={
        "required" : "Please Enter Password",
        "null" : "Please Enter Password",
        "blank" : "Please Enter Password",
        "min_length" : "Password Is Too Short",
        "max_length" : "Password Is Too Long",
    })

    def clean_username(self) -> str:

        username = self.cleaned_data.get("username")
        if UserModel.objects.filter(username = username).exists():
            raise forms.ValidationError("The Entred UserName Is Already Exists")

        return username
    
    def clean_email(self) -> str:

        email = self.cleaned_data.get("email")
        if UserModel.objects.filter(email = email).exists():
            raise forms.ValidationError("The Entred Email Is Already Exists")

        return email
    

    def save_data(self) -> AbstractBaseUser:

        user_object = UserModel.objects.create_user(
            username = self.cleaned_data["username"],
            email = self.cleaned_data["email"],
            password = self.cleaned_data["password"]
        )

        return user_object


class LoginForm(AuthForm):


    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop("request",None)
        super().__init__(*args,**kwargs)
        self.error_message:str = "No User Found With Entred Information"

    def clean(self) -> str:

        email:str = self.cleaned_data.get("email")
        password:str = self.cleaned_data.get("password")
        
        self.__found_user = authenticate(self.request,email = email,password = password)
        if not self.__found_user:
            raise forms.ValidationError(self.error_message)

        return self.cleaned_data
        

    @property
    def user(self) -> AbstractBaseUser:
        return self.found_user