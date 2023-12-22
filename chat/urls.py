from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='chat'

urlpatterns = [
    path('',views.ChatView,name='home'),
    path('signup/',views.SignupView,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='chat/login.html'),name='login'),
    
]
