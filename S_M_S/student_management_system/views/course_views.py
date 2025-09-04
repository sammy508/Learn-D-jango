

from ast import Delete
from functools import partial
import profile
from django.shortcuts import get_object_or_404
from yaml import serialize


from ..serializers.course_serializers import CourseSerializer
from ..models.course_model import CourseModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CourseApiView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request,pk=None):
        pass


    pass
