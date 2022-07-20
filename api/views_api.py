from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from django.contrib.auth.models import User

from datetime import date, datetime

# from .forms import MakerForm
from .models import AttandenceModel
from .serializers import ClockInSerializer, ClockOutSerializer

from usermodule.serializers import UserResponseSerializer

from .utility_helper import TimeCalculation
 



########################################################################################################
#### Added By: SHIFULLAH | Date: 18-JUL-2022
#### API for clock_in
########################################################################################################
class UserAttandanceAPI:
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) 
    def clock_in(request):
        """
            POST clock_in 
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        content = {}
        try:
            user_id = request.user.id
            # print("user:", user_id)

            username_exist_today = AttandenceModel.objects.filter(
                employee_id=user_id,
                to_date=date.today(),
            )

            user_details = User.objects.get(id=user_id)
            # print("###:  ",user_details)

            if len(username_exist_today) > 0:
                content['message'] = str(user_details.username)+', You are already in today.'
                content['status'] = status.HTTP_400_BAD_REQUEST
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            attandance_model = AttandenceModel( 
                employee_id = user_id,
                to_date = date.today(),
                in_time = datetime.now(),
                created_by = user_id,
                created_at = datetime.now() 
            )
            attandance_model.save()

            clock_in_id = attandance_model.id
            clock_in_qs = AttandenceModel.objects.filter(id=clock_in_id)
            clock_in_serializer = ClockInSerializer(clock_in_qs, many=True)

            user_data_qs = User.objects.filter(id=user_id) 
            user_data_serializer = UserResponseSerializer(user_data_qs, many=True)

            content['message'] = 'Success'
            content['status'] = status.HTTP_200_OK
            content["data"] = {"clock_in":clock_in_serializer.data[0], "user":user_data_serializer.data[0]}
            return Response(content, status=status.HTTP_200_OK)
        except Exception as ex:
            content['message'] = ex
            content['status'] = status.HTTP_404_NOT_FOUND
            content['data'] = {}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) 
    def clock_out(request):
        """
            POST clock_out 
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        content = {}
        try:
            user_id = request.user.id
            # print("user:", user_id)

            try:
                username_exist_today = AttandenceModel.objects.filter(
                    employee_id=user_id,
                    to_date=date.today(),
                )
            except:
                username_exist_today = None

            user_details = User.objects.get(id=user_id)
            # print("###:  ",username_exist_today)

            if not username_exist_today:
                content['message'] = str(user_details.username)+', You are not logged in today.'
                content['status'] = status.HTTP_400_BAD_REQUEST
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            
            for attendance in username_exist_today:
                # print("####### : ",attendance.in_time)
                attendance_id = attendance.id

                a_in_time = attendance.in_time 
                a_in_time = a_in_time.strftime("%Y-%m-%dT%H:%M:%SZ") 
                a_out_time = datetime.now()
                a_out_time = a_out_time.strftime("%Y-%m-%dT%H:%M:%SZ") 
                
                timeDiff = TimeCalculation.time_difference(a_in_time, a_out_time)
                time_hour_today = int(timeDiff)

            try:
                AttandenceModel.objects.filter(
                    id=attendance_id
                ).update(
                    out_time=datetime.now(),
                    total_hours=time_hour_today,
                    updated_by = user_id,
                    updated_at = datetime.now()
                )
            except Exception as ex:
                content['message'] = ex
                content['status'] = status.HTTP_404_NOT_FOUND
                content['data'] = {}
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            clock_in_qs = AttandenceModel.objects.filter(id=attendance_id)
            clock_in_serializer = ClockOutSerializer(clock_in_qs, many=True)

            user_data_qs = User.objects.filter(id=user_id) 
            user_data_serializer = UserResponseSerializer(user_data_qs, many=True)

            content['message'] = 'Success'
            content['status'] = status.HTTP_200_OK
            content["data"] = {"clock_in":clock_in_serializer.data[0], "user":user_data_serializer.data[0]}
            return Response(content, status=status.HTTP_200_OK)
        except Exception as ex:
            content['message'] = ex
            content['status'] = status.HTTP_404_NOT_FOUND
            content['data'] = {}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            
        }
    ))
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,)) 
    def attandence_details(request):
        """
            POST clock_out 
            Args:
                    request: HttpRequest object that contains metadata about the request

            Returns:
                JSON response containing message, status and data if applicable
        """

        content = {}
        try:
            user_id = request.user.id
            # print("user:", user_id)

            
            try:
                username_exist_today = AttandenceModel.objects.get(
                    employee_id=user_id,
                    to_date=date.today(),
                )
            except:
                username_exist_today = None

            user_details = User.objects.get(id=user_id)
            # print("###:  ",user_details)

            if not username_exist_today:
                content['message'] = str(user_details.username)+', You are not logged in today.'
                content['status'] = status.HTTP_400_BAD_REQUEST
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            clock_in_id = username_exist_today.id
            clock_in_qs = AttandenceModel.objects.filter(id=clock_in_id)
            clock_in_serializer = ClockOutSerializer(clock_in_qs, many=True)

            current_clock = datetime.today().strftime("%I:%M:%S %p")

            attnd_data = clock_in_serializer.data
            # print("$$$: ", attnd_data[0]["in_time"])
            
            a_in_time = attnd_data[0]["in_time"]
            if not attnd_data[0]["out_time"]:
                a_out_time = datetime.now()
                a_out_time = a_out_time.strftime("%Y-%m-%dT%H:%M:%SZ")
            else:
                a_out_time = attnd_data[0]["out_time"]
            
            timeDiff = TimeCalculation.time_difference(a_in_time, a_out_time)
            time_hour_today = int(timeDiff)
            # print("$$$: timeDiff: ",time_hour_today)
            AttandenceModel.objects.filter(
                id=username_exist_today.id
            ).update(
                total_hours = time_hour_today
            )

            today = datetime.today().strftime("%A")
            week_date_range = TimeCalculation.week_work_time(today)
            clock_in_qs = AttandenceModel.objects.filter(
                employee_id=user_id,
                to_date__range=(week_date_range[0], week_date_range[1])
            )
            week_hours = 0
            for data in clock_in_qs: 
                if (data.total_hours is None):
                    week_hours+=0
                else:
                    week_hours+=int(data.total_hours) 


            month_date_range = TimeCalculation.month_work_time()
            clock_in_qs = AttandenceModel.objects.filter(
                employee_id=user_id,
                to_date__range=(month_date_range[0], month_date_range[1])
            )
            month_hours = 0
            for data in clock_in_qs: 
                if (data.total_hours is None):
                    month_hours+=0
                else:
                    month_hours+=int(data.total_hours)

            user_data_qs = User.objects.filter(id=user_id) 
            user_data_serializer = UserResponseSerializer(user_data_qs, many=True)


            clock_data = clock_in_serializer.data[0]
            clock_data['current_clock'] = current_clock
            clock_data['today‌‌'] = time_hour_today                     
            clock_data['current_week'] = week_hours                     
            clock_data['current_month'] = month_hours                     
            
            out_data = {
                "clock_in":clock_data,
                "user":user_data_serializer.data[0] 
            }

            content['message'] = 'Success'
            content['status'] = status.HTTP_200_OK
            content["data"] = out_data
            return Response(content, status=status.HTTP_200_OK)
        except Exception as ex:
            content['message'] = ex
            content['status'] = status.HTTP_404_NOT_FOUND
            content['data'] = {}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

