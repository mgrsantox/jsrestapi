from rest_framework import serializers
from studentapp.models import Students


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
