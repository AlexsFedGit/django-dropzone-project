from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from home.models import Image


def home(request):
    images = Image.objects.all()
    context = {
        'images': images
    }
    return render(request, 'index.html', context)


def file_upload(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        if my_file:
            # my_file.name
            Image.objects.create(image=my_file)
            return HttpResponse('')
        else:
            return HttpResponse(
                '<h1>500 Internal Server Error (Внутренняя ошибка сервера)</h1>',
                status=500)
    return JsonResponse({'post': 'false'})
