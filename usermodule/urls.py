from . import views_api
from django.urls import path

urlpatterns = [      
    path('web/create_user/', views_api.UserListAPI.create_user),     
]
