from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['GET'], url_path='retrieve-by-user')
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'user_id',
                openapi.IN_QUERY,
                description="ID of the user",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ]
    )
    def retrieve_by_user(self, request):
        """
        Retrieve a specific user and their associated tasks using user_id as a query parameter
        """
        # Explicitly print query params for debugging
        print("Query Params:", request.query_params)

        # Ensure the correct retrieval of user_id
        user_id = request.query_params.get('user_id', None)

        # Validate user_id presence
        if not user_id:
            return Response(
                {"error": "user_id query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize user data
        user_serializer = UserSerializer(user)

        # Retrieve tasks assigned to the user
        tasks = Task.objects.filter(assigned_users=user)
        task_serializer = TaskSerializer(tasks, many=True)

        # Return combined data
        return Response({
            "user": user_serializer.data,
            "tasks": task_serializer.data
        })


    @action(detail=True, methods=['PATCH'])
    def complete_task(self, request, pk=None):
        """
        Mark a specific task as completed
        """
        task = self.get_object()
        task.mark_completed()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer