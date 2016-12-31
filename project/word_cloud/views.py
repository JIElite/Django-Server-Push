from django.shortcuts import render

# Create your views here.
def word_cloud(request):
    return render(request, 'index.html')
