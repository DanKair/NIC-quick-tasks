from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Responds for Create (POST) operation and has additional DELETE all Tasks functionality
class TaskCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        Task.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskUpdateDelete(generics.RetrieveUpdateDestroyAPIView): #RetrieveUpdateDestroy allow us to Update and Delete items
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # looking for primary key, which stands for item id
    lookup_field = "pk"