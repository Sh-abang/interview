from django.shortcuts import render
from . models import CustUsers
from rest_framework import viewsets
from rest_framework import permissions
from populate.serializers import UserSerializer

# Create your views here.

def index(request):
    users_list = CustUsers.objects.all()
    context = {'users_list': users_list}
    return render(request, "populate/index.html",context)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustUsers.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]