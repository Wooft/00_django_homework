import os.path
import pathlib
import csv
import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    list_stations = []
    path = pathlib.Path.cwd()
    with open(file=os.path.join(path, 'data-398-2018-08-30.csv'), encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations = {
                'name': row['Name'],
                'street': row['Street'],
                'district': row['District']
            }
            list_stations.append(stations)
    paginator = Paginator(list_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'stations/index.html', context)
