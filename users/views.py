from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('date_joined')
    permission_classes = [IsAuthenticated, ]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
