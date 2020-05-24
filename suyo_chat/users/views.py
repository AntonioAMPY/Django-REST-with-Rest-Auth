from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class ListCreateUserAPIView(ListCreateAPIView):
    """This view allow list and create users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny,)
