from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, testPageView, loginpageview, RegisterPageView


urlpatterns = [
   
    path('about/', AboutPageView.as_view(), name='about'),
    path('test/', testPageView.as_view(), name='test'),
    path('', HomePageView.as_view(), name='home'),
    path('login/', loginpageview.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='registerpage'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path(r'^', views.button),
    path(r'^output$', views.output, name='script'),
    #path('test/', views.input, name="input"),
    #path('test/', views.input),
    #path('', views.index, name='index'),
    
    
    
    
]