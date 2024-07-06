from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'task/index.html')

def modal_create(request):
    return render(request, 'task/modal_create.html')