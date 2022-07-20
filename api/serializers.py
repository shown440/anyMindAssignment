from rest_framework import serializers

class ClockInSerializer(serializers.Serializer):
    employee_id      = serializers.IntegerField()
    to_date          = serializers.DateField()
    in_time          = serializers.DateTimeField() 


class ClockOutSerializer(serializers.Serializer):
    employee_id      = serializers.IntegerField()
    to_date          = serializers.DateField()
    in_time          = serializers.DateTimeField() 
    out_time          = serializers.DateTimeField() 