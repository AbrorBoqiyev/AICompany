from django.shortcuts import render

# Create your views here.
def myapp(request):
    return render(request, 'myapp.html', context={'name':'hello'})

def about(request):
    return render(request, 'about.html')

