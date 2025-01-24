
from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home, name="home"),
    path('',views.about, name="about"),
    path('',views.login, name="login"),
    path('',views.service, name="service"),

]