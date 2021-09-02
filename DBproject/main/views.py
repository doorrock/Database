from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    if request.method == "GET":
        return render(request, 'main.html')