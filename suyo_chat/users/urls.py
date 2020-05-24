from django.urls import path
from users.views import ListCreateUserAPIView


urlpatterns = [
    path(
        'user/',
        ListCreateUserAPIView.as_view(),
        name='user'
    ),
]
