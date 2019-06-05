from django.shortcuts import render, redirect
from .forms import *
from .models import Image
import sys
from PIL import Image as ChangeImage
# Create your views here.

def lending(request):
    images = Image.objects.all()
    return render(request, 'main_page.html', context={'images': images})


"""Обработка формы на странице upload"""
def upload(request):
    if request.method == 'POST':
        upload_form = UploadForm(data=request.POST, files=request.FILES)
        if upload_form.is_valid():

            upload_form.save()
            return redirect('/')
    else:
        upload_form = UploadForm()
    context = {
        'form': upload_form,
    }
    return render(request, 'upload_page.html', context)

"""Обработчик страницы картинки"""
def image_page(request, id):
    """
    Берется картика из БД и сохраняется во временной переменной
    """
    image = Image.objects.get(id=id)
    context = {}
    get = request.GET
    changed_image = ChangeImage.open(image.image.url[1:])
    width = changed_image.size[0]
    height = changed_image.size[1]
    #Обработка GET запроса
    if get.get('width'):
        width = get.get('width')
    if get.get('height'):
        height = get.get('height')
    changed_image = changed_image.resize((int(width), int(height)), ChangeImage.ANTIALIAS)
    #Сохранение изображения во временной переменной, с настройкой качества в кБайт
    if get.get('size'):
        if image.image.url.find('.jpg') != -1:
            changed_image.save('media/images/changed_image.jpg', quality=int(get.get('size')))
            context = {'image': '/media/images/changed_image.jpg'}
        elif image.image.url.find('.png') != -1:
            changed_image.save('media/images/changed_image.png', quality=int(get.get('size')))
            context = {'image': '/media/images/changed_image.png'}
    else:
        if image.image.url.find('.jpg') != -1:
            changed_image.save('media/images/changed_image.jpg')
            context = {'image': '/media/images/changed_image.jpg'}
        elif image.image.url.find('.png') != -1:
            changed_image.save('media/images/changed_image.png')
            context = {'image': '/media/images/changed_image.png'}

    return render(request, 'image_page.html', context)
