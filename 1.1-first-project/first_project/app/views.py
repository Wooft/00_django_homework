import pathlib

from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir_view')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # Добавил HTML шаблон
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    return render(request, 'app/current_time.html', {'time': current_time})

def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = pathlib.Path.cwd()
    list_files = os.listdir(path)
    return render(request, 'app/workdir_view.html', {'workdir_files': list_files})
    raise NotImplemented
