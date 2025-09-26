

from tkinter import EXCEPTION
from jsonschema import ValidationError
from rest_framework.response import Response
from rest_framework import generics, status
from yaml import serialize
from .sem_serializers import SemesterSerializers
from ..models.semester_models import SemesterModel
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser



class SemesterApiView(generics.GenericAPIView):
    parser_classes = [JSONParser]
    queryset = SemesterModel.objects.all()

    permission_classes =[AllowAny]  # have to change later to adminuser only
    serializer_class = SemesterSerializers


    def post(self,request,*args,**kwargs):

        serializer = self.get_serializer(data= request.data)

        try:
            serializer.is_valid(raise_exception=True)   # by using this raise_exception we dont need to use if condition
            serializer.save()
            return Response(
                {"message":"Semester Created Sucessfully"},
                serializer.data, status=201
            )
            

        except ValidationError as e :
            return Response(
                {"error": "Invalid data", "details": e.detail},
                status=400
            )
        except Exception as e:
            return Response(
                {"error": "Something went wrong", "details": str(e)},
                status=500
            )
            
    
    def get(self,request,*args,**kwargs):

        try:
                sem_data = self.get_queryset()

                if not sem_data.exists():
                    return Response(
                        {"message":"No data found"},
                        status = status.HTTP_200_OK
                    )
                serializer = SemesterSerializers(instance=sem_data, many=True)
                return Response(
                    {
                            "count": sem_data.count(),
                            "courses": serializer.data
                        },
                        status=status.HTTP_200_OK
                )
        
        except Exception as e:
            return Response({"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             

class SingleSemesterView(generics.GenericAPIView):
    permission_classes =[AllowAny]  # have to change later to adminuser only
    serializer_class = SemesterSerializers

    def get(self, request, pk, *args,**kwargs):

        sem_data = get_object_or_404(SemesterModel, pk=pk)
        serializer = SemesterSerializers(sem_data)
        return Response(
              {
                     "message":"Subject data fetched sucessfully",
                      "data":serializer.data
                },
                
                     status=status.HTTP_200_OK
        )
    

    def put(self, request, pk, *args,**kwargs):
        sem_data = get_object_or_404(SemesterModel, pk=pk)
        serializer = SemesterSerializers(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Semester data updated Sucessfully!",
                },
                status= status.HTTP_201_CREATED
            )
        return Response(
            {"error": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST
               )


    def delete(self, request, pk, *args,**kwargs):
        try:
             sem_data = get_object_or_404(SemesterModel, pk=pk)
             sem_data.delete()
             return Response({"message": f"Subject with id {pk} deleted successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



