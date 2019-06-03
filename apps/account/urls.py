from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test, name='test'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name='logout'),
]