from .models import RegistrationModel
from rest_framework import serializers



class Regist_Serializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields= '__all__'