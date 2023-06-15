from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from django.http import *


def index(request):
    if request.POST:
        input_text = request.POST['inp_message']
        






    return render(request,'chatbotapp/index.html')
