from rest_framework import generics
from accounts.serializers import UserDetailSerializer, UsersListSerializer
from main.models import CustomUser

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer

class UsersListView(generics.ListAPIView):
    serializer_class = UsersListSerializer
    queryset = CustomUser.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = CustomUser.objects.all()

def is_staff_user(user):
    return user.is_authenticated and user.is_staff
