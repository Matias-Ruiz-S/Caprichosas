from django.shortcuts import render

def home(request):    
    return render(request, 'core/index.html')

def template(request):    
    return render(request, 'core/template.html')