from django.shortcuts import render, HttpResponse

# Create your views here.
def hello_world(request):

    return HttpResponse('<b>Testa</b>', status=200)