

from django.shortcuts import render
from django.views import View


class AuthenticateView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = "user/authenticate.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self,request):
        pass
    