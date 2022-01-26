from django.shortcuts import render

def index(request):
    data={}
    url="./templates/index.html"
    return render(request,url,data)