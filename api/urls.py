from . import views, views_api
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    ########## API #########################
    path('login/', views.CustomLoginView.as_view(), name='my_custom_login'),
    path('api-token-refresh/', refresh_jwt_token, name='my_refresh_token'), 

    # ########## WEB API ##################### 
    path('clock_in/', views_api.UserAttandanceAPI.clock_in, name='clock_in'),
    path('clock_out/', views_api.UserAttandanceAPI.clock_out, name='clock_out'),
    path('attandence_details/', views_api.UserAttandanceAPI.attandence_details, name='attandence_details'),
    
]
