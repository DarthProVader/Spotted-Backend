from django.urls import path
from .views import CarList, CarDetail, UserList, UserDetail

urlpatterns = [
    path('car/', CarList.as_view()),
    path('car/<int:pk>/', CarDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
] 