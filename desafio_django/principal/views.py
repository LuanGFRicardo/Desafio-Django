from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'principal/home.html')

def image_url(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        return render(request, 'principal/image_url.html', {'image_url': image_url})
    return render(request, 'principal/image_url.html')
