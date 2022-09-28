from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Car, User
from .serializers import CarSerializer, UserSerializer


class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Car.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser, FormParser)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)
