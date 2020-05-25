from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from users.serializers import CreateUserSerializer, ListUserSerializer


class CreateUsersAPIView(CreateAPIView):
    """This view allow create users."""
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class ListUsersAPIView(ListAPIView):
    """This view allow list all users."""
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
