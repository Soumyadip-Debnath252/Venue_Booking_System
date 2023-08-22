from django.shortcuts import render, Http404, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')  

def catalouge(request):
    return render(request, 'myapp/gallery.html')
   
def Registration(request):
    return render(request, 'myapp/services.html')  
       