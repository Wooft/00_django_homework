import pprint

from django.shortcuts import render
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


list_dates = []
books = Book.objects.all().order_by('-pub_date')
for book in books:
    if book.pub_date.strftime('%Y-%m-%d') not in list_dates:
        #создаем список всех уникальных дат публикации по маске
        list_dates.append(book.pub_date.strftime('%Y-%m-%d'))
print(list_dates)

#Выводит список книг за дату публикации
def show_books_from_date(request, pub_date):
    template = 'books/books_from_date.html'
    books = Book.objects.filter(pub_date=pub_date).all()
    #находим индекс предыдущей даты, если она есть. Если её нет, то возвращаем None
    if list_dates.index(pub_date) < len(list_dates) - 1:
        previous_date = list_dates[list_dates.index(pub_date) + 1]
    else:
        previous_date = None
    #Находим индекс следующей даты в списке, если индекс равен 0, то присваиваем следующей дате None
    if list_dates.index(pub_date) == 0:
        next_date = None
    else:
        next_date = list_dates[list_dates.index(pub_date) - 1]
    context = {
        'content': [
            books,
            next_date,
            previous_date
        ]
    }
    print(context['content'][1], context['content'][2])
    return render(request, template, context)