from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Student
from accounts.api.serializers import StudentSerializer, StudentRegisterSerializer



@api_view(['POST'])
def register_student(request):
    if request.method == "POST":
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRegistrationAPIView1(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class StudentRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)