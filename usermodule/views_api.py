from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# from .models import UserModuleProfile 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core import serializers

import json

# from api import proj_utils
from .serializers import UserSerializer, UserResponseSerializer




########################################################################################################
#### Added By: SHIFULLAH | Date: 12-DEC-21
#### WEB API for user_list  
########################################################################################################
class UserListAPI:
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'length': openapi.Schema(type=openapi.TYPE_INTEGER, description='length'), 
            'start': openapi.Schema(type=openapi.TYPE_INTEGER, description='start'), 
            'draw': openapi.Schema(type=openapi.TYPE_INTEGER, description='draw'), 
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='user_id'), 
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,))
    def get_user_list(request):
        """
            Get user_list
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        pass
    
    #################################################################### 
    #### WEB API for user_details
    #####################################################################
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'), 
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) # IsAuthenticated,
    def get_user_details(request):
        """
            Get user_details
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        pass


    #################################################################### 
    #### WEB API for create_user
    #####################################################################
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='User Name'), 
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'), 
            'password1': openapi.Schema(type=openapi.TYPE_STRING, description='Password1'), 
            'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'), 
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) # IsAuthenticated,
    def create_user(request):
        """
            POST create_user
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        content = {} 
        required_field_list = ['username', 'email', 'password1', 'password2']
        empty_data_list = []
        for temp in required_field_list:
            if request.data[temp] == None or request.data[temp] == '':
                empty_data_list.append(temp)
        if empty_data_list: 
            content['message'] = 'Please fill up the required fields.'
            content['status'] = status.HTTP_400_BAD_REQUEST
            return Response(content, status=status.HTTP_404_NOT_FOUND) 
        
        try: 
            data = request.data
            # print("############### data: ", data)
            
            serializer = UserSerializer(data=data)
            if serializer.is_valid(): 
                user_code = data['username'] 
                email = data['email'] 
                password1 = str(data['password1'])
                password2 = str(data['password2'])  

                if password1 != password2: 
                    content['message'] = 'Password doesnot match!!!'
                    content['status'] = status.HTTP_400_BAD_REQUEST
                    return Response(content, status=status.HTTP_404_NOT_FOUND)

                username_exists = User.objects.filter(username=user_code)
                # print("username_exists: ",len(username_exists))
            
                if len(username_exists) > 0:
                    username_exists_status =  True
                else:
                    username_exists_status = False

                if username_exists_status:
                    content['message'] = 'This user is already exist'
                    content['status'] = status.HTTP_400_BAD_REQUEST
                    return Response(content, status=status.HTTP_404_NOT_FOUND)
                
                user_model = User( 
                    username = user_code,
                    email = email,
                    password = make_password(password1),
                    is_superuser = False,
                    is_active = True,
                    is_staff = True
                )
                user_model.save()

                new_user_id = user_model.id
            else:
                content['message'] = 'Please provide valid data'
                content['status'] = status.HTTP_400_BAD_REQUEST
                return Response(content, status=status.HTTP_404_NOT_FOUND) 

            user_data_qs = User.objects.filter(id=new_user_id) 
            # user_data = serializers.serialize('json', list(user_data_qs),fields=('username','email'))
            user_data_serializer = UserResponseSerializer(user_data_qs, many=True) 

            content['message'] = 'Success'
            content['status'] = status.HTTP_200_OK
            content['data'] = user_data_serializer.data[0]    #json.loads(user_data)[0]
            return Response(content, status=status.HTTP_200_OK)
        except Exception as ex:
            content['message'] = str(ex)
            content['status'] = status.HTTP_404_NOT_FOUND
            content['data'] = {}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


    #################################################################### 
    #### WEB API for edit_user_details
    #####################################################################
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'), 
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) # IsAuthenticated,
    def edit_user_details(request):
        """
            POST edit_user_details
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        pass


    ###########################################################################
    #### Added By: SHIFULLAH 
    #### WEB API for delete_user
    #############################################################################
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'), 
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,))
    def delete_user(request):
        """
            Get delete_user
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        pass


