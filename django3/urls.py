"""django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import  settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from django.contrib.auth import  views as auth_views
from tasks.views import  home 


handler404 = 'django3.views.handler404'
handler500 = 'django3.views.handler500'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('tasks/', include('tasks.urls',namespace='tasks')),
    path('account/', include('accounts.urls',namespace='accounts')),

    #auth view
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
    name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
    name="password_reset_complete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




