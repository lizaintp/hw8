from django.urls import path
from apps.users.views import login, forgot_password, register

urlpatterns = [
    path('', forgot_password, name = 'forgot_password'),
    path('register', register, name = 'register'),
    path('login/', login, name = 'login'),
    
    
]
    