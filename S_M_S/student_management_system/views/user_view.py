


from django.shortcuts import get_object_or_404
from ..models.user_models import UserModel
from ..serializers.User_serializer import Userserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserApiview(APIView):

    def get(self, request, pk=None):
        try:

            if pk:   # if primary key is provided for single user

                user_data = get_object_or_404(UserModel, pk=pk)
                serializer = Userserializer(user_data, many=True)

                return Response(
                    serializer.data, status= status.HTTP_200_OK
                )
            else:
                user_data = UserModel.objects.all()
                serializer = Userserializer(user_data, many=True)

                return Response(
                    serializer.data, status= status.HTTP_200_OK
                )
        except UserModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = Userserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status = status.HTTP_201_CREATED
            )
        return Response(
            status= status.HTTP_400_BAD_REQUEST
        )
    