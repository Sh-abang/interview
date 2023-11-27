# from django.contrib.auth.models import User, Group
from .models import CustUsers
from rest_framework import serializers

# 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustUsers
        fields = ['id_number', 'email', 'mobile_number', 'full_names','designation','occupation','Nationality','income_source','res_address','post_address','appoint_date']
