from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View Function - Takes in a request returns a response
# Request Handler

def say_hello(request):
    return render(request, 'hello.html')