from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
def Home(request):
    return render(request,'Home.html')
def chat(request):
    return render(request,'chat.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def prime(request):
    return render(request,'prime.html')
def about(request):
    return render(request,'about.html')
