from rest_framework import serializers
from .models import event_model


class event_serializers (serializers.ModelSerializer):

    class Meta :

        model = event_model
        fields = '__all__'