

from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.http.response import HttpResponse

from .forms import RegisterForm,LoginForm

class AuthenticateView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = "user/authenticate.html"
        self.context = {}

    def get(self, request):

        return render(request, self.template_name)
    


class RegisterView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name:str = "user/authenticate.html"
        self.context = {}

    def post(self,request) -> HttpResponse:
        
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save_data()
            return redirect("/")
        
        self.context["register_form"] = register_form
        return render(request,self.template_name,self.context)
        
class LoginView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name:str = "user/authenticate.html"
        self.context = {}

    def post(self,request) -> HttpResponse:

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            
            found_user = login_form.user
            login(request,found_user)
            return redirect("/")
        
        self.context["login_form"] = login_form
        return render(request,self.template_name,self.context)

