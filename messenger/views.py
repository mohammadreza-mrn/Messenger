
from django.shortcuts import redirect
from django.views import View

class HomeView(View):

    def get(self,request):
        
        if request.user.is_authenticated:

            return redirect("")
        
        return redirect("user:auth-view")