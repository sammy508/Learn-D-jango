
from functools import partial
from rest_framework.exceptions import ValidationError, NotFound
from .teacher_serializer import TeacherSerializer
# from .teacher_models import TeacherModel
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import traceback
from .teacher_model import TeachersModel

class TeacherView(GenericAPIView):
    queryset = TeachersModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


    def post(self,request, *args, **kwargs):
        try:

            serializer = self.get_serializer(data = request.data)
            serializer.is_valid()
            serializer.save()
            return Response(
                {"message": "Teacher created sucessfully"}, status= status.HTTP_201_CREATED
            )
       
        except ValidationError as e:
            return Response(
                {"error":"Validation error", 
                 "details":e.detail,
                 }, 
                 status= status.HTTP_400_BAD_REQUEST

            )
        except Exception as e:
       
            print(traceback.format_exc())  # log full traceback in console
            return Response(
                {"error": "Something went wrong!", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    
    def get(self, request, *args, **kwargs):
        try:
            data = self.get_queryset()

            if not data.exist():
                raise NOtFound("No item Found")

            serializer = self.get_serializer(data, many =True)
            return Response(
                serializer.data, status= status.HTTP_200_OK
            )
        
        except NotFound as nf:
            return Response(
                {"error":str(nf)}, status= status.HTTP_404_NOT_FOUND

            )
        
        except Exception as e:
            return Response(
                {"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def put(self,request,pk=None,*args,**kwargs):
        try:   
            teacher_data = self.get_queryset().filter(pk=pk).first()

            if not teacher_data():
                    raise NOtFound("Iten with id {pk} not found")
            
            serializer = self.get_serializer(teacher_data, data = request.data, partial=True)
            serializer.is_valid()
            return Response(
                {"message":"Teacher's data updated sucessfully! "},
                serializer.data, status= status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {"error": "Something went wrong", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def delete(self, request, pk, *args, **kwargs):

        try:
            Teacher_data = self.get_queryset().filter(pk=pk).first()

            if not Teacher_data:
                return Response(
                    "Item with id {pk} not found."
                )
            
            Teacher_data.delete()
            return Response({"message": f"Item {pk} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e :
            return Response(
                {"error": "Something went wrong", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR

            )



    
