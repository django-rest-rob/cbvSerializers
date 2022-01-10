from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 3

# WAY FOUR: Using VIEWSETS
# ONLY 1 Class will implement both KEY and NON-KEY operations
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination

"""
# WAY THREE: Using GENERICS
# 1. CBV for NON-PK operations
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# 2. CBV for PK operations
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
"""

"""
# WAY TWO:
# 1. CBV for NON-PK operations
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # GET - get all
    def get(self, request):
        return self.list(request)

    # POST - create
    def post(self, request):
        return self.create(request)

# 2. CBV for PK operations
class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # GET - get single
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # PUT - update single
    def put(self, request, pk):
        return self.update(request, pk)

    # DELETE - delete single
    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

"""
#WAY ONE:
# 1. CBV for NON-PK operations
class StudentList(APIView):
    # GET
    def get(self, request):
        # get from db using Model
        students = Student.objects.all()
        # make a StudentSerializer and pass the returned data
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # POST
    def post(self, request):
        # first deserialize the sent data from the POST request
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 1. CBV for PK operations
class StudentDetail(APIView):

    # Method for getting Student object
    def get_object(self, pk):
        try:
            # get the Student from Model with pk
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    # GET - single Student
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # PUT
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


























#
