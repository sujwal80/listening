from django.contrib import admin
from django.urls import path, include
from musicApp import views

urlpatterns = [
    path('', include('musicApp.urls')),
    path('admin/', admin.site.urls),
    path('account/login/', views.signin, name="login_page"),
    path('account/signup/', views.signup, name="signup_page"),
    path('account/logout/', views.signout, name="logout_page")
]
