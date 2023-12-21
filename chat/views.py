from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import SignupForm
import traceback
# Create your views here.
def ChatView(request):
    return render(request,'chat/home.html')

def SignupView(request):
    if request.POST:
      form=SignupForm(request.POST)

      try:

        if form.is_valid():
            form.save()
            print(form.save())
            

            return redirect('/')
        else:
           print(form.errors)
           
      except Exception as e:
            print(f"Error in SignupView: {e}")

    else:
      form=SignupForm()

    return render(request,'chat/signup.html',{
        'form':form
    })