from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee 
        field = '__all__'


    
    