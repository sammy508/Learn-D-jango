from token import tok_name
import token
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.logout_serializer import UserLogoutSerializer

class UserLogoutViews(generics.GenericAPIView):
    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.IsAuthenticated]



    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)   # Blacklist the refresh token
            token.blacklist() 
            return Response({'message': 'Logged out successfully'}, 
                            
                            status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Invalid token'}, 
                            status=status.HTTP_400_BAD_REQUEST)
