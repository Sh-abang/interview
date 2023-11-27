from django.shortcuts import render
from . models import CustUsers
from django.views import generic
import pandas as pd

# Create your views here.
def index(request):
    users_list = CustUsers.objects.all()
    context = {'users_list': users_list}
    return render(request, "populate/index.html",context)

    # def collectFromExcel(self, df):