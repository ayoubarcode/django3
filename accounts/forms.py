from django import  forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User



class UserCreationForCusomize(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={
            "class":"form-control mb-4",
            "placeholder":"username"}),

            'email':forms.EmailInput(attrs={
            "class":"form-control mb-4",
             "placeholder":"Email"}),

            'first_name':forms.TextInput(attrs={
            "class":"form-control mb-4",
             "placeholder":"First Nme"}),

            'last_name':forms.TextInput(attrs={
            "class":"form-control mb-4",
             "placeholder":"Last Name"}),

            'password1':forms.PasswordInput(attrs={
            "class":"form-control", 
            "placeholder":"password"}),

            'password2':forms.PasswordInput(attrs={
            "class":"form-control", 
            "placeholder":"password"}),

           
        }
