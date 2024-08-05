from django.shortcuts import render

# Create your views here.
def myapp(request):
    return render(request, 'myapp.html')

def home(request):
    context = {
        'name': 'World',
    }
    return render(request, 'index.html', context)