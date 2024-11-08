from django.shortcuts import render, HttpResponse, redirect

from time import asctime, strftime

from string import ascii_lowercase
from random import sample

from django.http import HttpResponse
from os import getcwd,  listdir,  remove

# Create your views here.


def index(request):
    return HttpResponse("<h1> Bookstore <h1>")


def get_book(request, book_name):
    return HttpResponse(f"<h1> {book_name} <h1>")


def get_year(request, year_id):
    return HttpResponse(f"<h1> {year_id} <h1>")


def current_time(request):
    return HttpResponse(f' {asctime().split()[3:]} ')


def workdir(request):
    return HttpResponse(f' {getcwd()} ')


def filelist(request):
    return HttpResponse(f' {listdir()} ')

def create_files(request):
    for _ in range(10):
        filename = ''.join(sample(ascii_lowercase, 10)) + '.txt'
        print(filename)
        f = open('filename', 'w')
        f.write(f'Hello, from {filename}')
    return HttpResponse(f' {listdir()} ')


def del_txt_files(request):
    for file in listdir():
        if file.endswith('.txt'):
            remove(file)
    return HttpResponse(f' {listdir()} ')


def show_url(request):
    return HttpResponse(f' {request.get_full_path()} ')


def calculator(request, val_1 , val_2):
    return HttpResponse(f' {val_1}  + {val_2} = {val_1 + val_2}')

def f404(request, info):
    return HttpResponse(f'Непонятный адрес {info}')

def smart_calc(request, string):
    try:
        print(string)
        res = eval(string)
        return HttpResponse(f'<h1> Выражение {string} = {res} </h1>')
    except:
         return HttpResponse(f'Непонятный адрес {string}')
        #   return redirect('f404')


def get_requests(request):
    requests = request.__dict__
    print(request)
    return HttpResponse(f' {requests} ')