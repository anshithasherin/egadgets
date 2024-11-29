from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.views import View
from .forms import Loginform,Regform
from  django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView
from django.urls import reverse_lazy

# Create your views here.
# class LandingView(View):
#     def get(self,request):
#         return render(request,'landing.html')
class LandingView(TemplateView):
    template_name='landing.html'
    
# class LoginView(View):
#      def get(self,request):
#         form=Loginform()
#         return render(request,'login.html',{"form":form})
#      def post(self,request,**kwargs):
#          formdata=Loginform(data=request.POST)
#          if formdata.is_valid():
#             uname=formdata.cleaned_data.get('username')
#             pswd=formdata.cleaned_data.get('password')
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 return redirect('home')
                
#             else:
#                 messages.error(request,'login')
#                 return redirect('log')
#          return render(request,'login.html',{"for,":formdata})
class LoginView(FormView):
    template_name='login.html'
    form_class=Loginform
    def post(self,request,**kwargs):
         formdata=Loginform(data=request.POST)
         if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('home')
                
            else:
                messages.error(request,'login')
                return redirect('log')
         return render(request,'login.html',{"for,":formdata})

    
     
# class RegView(View):
#     def get(self,request):
#         form=Regform()      
#         return render(request,'reg.html',{'form':form})
#     def post(self,request,**kwargs):
#         formdata=Regform(data=request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             messages.success(request,'Registration Successfull!')
#             return redirect('log')
#         messages.error(request,'registration Failed!!')
#         return render(request,'reg.html',{"form":formdata})

class RegView(CreateView):
    template_name='reg.html'
    form_class=Regform
    success_url=reverse_lazy('log')
    def form_valid(self, form):
        messages.success(self.request,'success fully registered')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Something went wrong')
        return super().form_invalid(form)
            
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

     
    
