from rest_framework import serializers
from center.events.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'posts_count', 'events']
        depth = 1
        exclude = ['created_by', ]
