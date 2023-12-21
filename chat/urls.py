from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='chat'

urlpatterns = [
    path('',views.ChatView,name='home'),
    path('signup/',views.SignupView,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]
