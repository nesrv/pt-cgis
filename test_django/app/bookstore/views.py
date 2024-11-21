from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from .forms import BookForm


def index(request):    
    return HttpResponse("Bookstore")


# book1 = Book(title='Муму', author='Тургенев', price=10)
# book2 = Book(title='Мастер и Маргарита', author='Булгаков', price=15)
# book3 = Book(title='Евгений Онегин', author='Пушкин', price=20)
# book4 = Book(title='Война и мир', author='Толстой', price=25)

# book1.save()
# book2.save()
# book3.save()
# book4.save()


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})
    



