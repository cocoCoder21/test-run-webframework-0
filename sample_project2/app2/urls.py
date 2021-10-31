from django.urls import path
from . import views

#TEMPLATE TAGGING
app_name = 'app2'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
