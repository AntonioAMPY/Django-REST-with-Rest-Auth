from django.urls import path
from users.views import CreateUsersAPIView, ListUsersAPIView


urlpatterns = [
    path(
        '',
        ListUsersAPIView.as_view(),
        name='list-users'
    ),
    path(
        'registration',
        CreateUsersAPIView.as_view(),
        name='create-users'
    ),
]
