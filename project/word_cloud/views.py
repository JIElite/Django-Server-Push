from django.shortcuts import render

# Create your views here.
def word_cloud(request):
    return render(request, 'index.html')

def topic_cloud(request):
    return render(request, 'topic_cloud.html')
