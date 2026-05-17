from rest_framework import serializers
from .models import Company

class companySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model:Company
        