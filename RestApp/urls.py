from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('hello/',views.HelloView.as_view(),name = "hello" ),
    path('pruebaGetInfoUser/',views.pruebaGetInfoUser.as_view(),name = "pruebaGetInfoUser" ),
    path('Users/',views.ListUser.as_view(),name = "ListUser" ),
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]