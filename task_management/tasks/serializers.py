from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']
        extra_kwargs = {
            'email': {'required': False},
            'mobile': {'required': False}
        }

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=User.objects.all(), 
        write_only=True, 
        source='assigned_users'
    )

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'created_at', 
            'completed_at', 'task_type', 'status', 
            'assigned_users', 'assigned_user_ids'
        ]
        read_only_fields = ['created_at']

    def create(self, validated_data):
        """
        Custom create method to handle many-to-many relationship
        """
        assigned_users = validated_data.pop('assigned_users', [])
        task = Task.objects.create(**validated_data)
        
        for user in assigned_users:
            task.assigned_users.add(user)
        
        return task