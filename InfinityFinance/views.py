from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def missing_404_page(request, exception):
    return render(request, '404.html', status=404)