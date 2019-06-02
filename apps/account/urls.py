from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name='logout'),
]