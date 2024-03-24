from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .serializer import StudentSerializer
from viewapp.models import Student

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGenericView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    