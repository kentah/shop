from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    message = 'This is the main page'
    context = {'message': message}
    return render(request, 'store/index.html', context)

def about(request):
    return HttpResponse('This is the about page')

def gallery(request):
    return HttpResponse('This is the gallery page')

def shop(request):
    return HttpResponse('This is the shop page')

def join(request):
    return HttpResponse('This is the page on which you set up your account')

def sign_in(request):
    return HttpResponse('This is where you sign in')

def terms(request):
    return HttpResponse('This displays the terms of the site')

def privacy(request):
    return HttpResponse('This is the privacy statement')
