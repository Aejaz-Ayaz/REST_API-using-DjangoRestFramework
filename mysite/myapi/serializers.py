from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'aliasname')
