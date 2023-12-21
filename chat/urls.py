from django.urls import path
from . import views

app_name='chat'

urlpatterns = [
    path('',views.ChatView,name='home'),
    path('signup/',views.SignupView,name='signup')
]
