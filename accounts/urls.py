from django.urls import path
from .views import  login,register,logoutuser

app_name='accounts'
urlpatterns = [
    path('login',login, name="login" ),
    path('register',register, name="register" ),
    path('logout',logoutuser, name="logout" ),
]
