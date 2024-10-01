from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blogs(request):
    return render(request, 'blogs.html')

def BlogTemplate1(request):
    return render(request, 'BlogTemplate1.html')

def BlogTemplate2(request):
    return render(request, 'BlogTemplate2.html')

def BlogTemplate3(request):
    return render(request, 'BlogTemplate3.html')

