from django.shortcuts import render
from select_image.forms import PicForm
from select_image.models import ImgFiles


def home(request):
    if request.method == "POST":
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'home.html', context)
    context = {'form': PicForm()}
    return render(request, 'home.html', context)


def img_list(request):
    images = ImgFiles.objects.all()
    context = {'images': images}
    return render(request, 'list.html', context)


def img_ent(request):
    images = ImgFiles.objects.all()
    context = {'images': images}
    return render(request, 'list_ent.html', context)


def img_premium(request):
    images = ImgFiles.objects.all()
    context = {'images': images}
    return render(request, 'list_premium.html', context)
