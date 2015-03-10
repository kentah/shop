from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    msg = 'This is the main page'
    context = {'msg': msg}
    return render(request, 'store/index.html', context)

def about(request):
    msg = 'This is the "about" page'
    context = {'msg': msg}
    return render(request, 'store/about.html', context)

def gallery(request):
    msg = 'This is the gallery page'
    context = {'msg': msg}
    return render(request, 'store/gallery.html', context)

def shop(request):
    msg = 'This is the shopping page'
    context = {'msg': msg}
    return render(request, 'store/shop.html', context)

def join(request):
    msg = 'This is where you sign up to join'
    context = {'msg': msg}
    return render(request, 'store/join.html', context)

def sign_in(request):
    msg = 'This is where users log in'
    context = {'msg': msg}
    return render(request, 'store/sign_in.html', context)

def terms(request):
    return HttpResponse('This displays the terms of the site')

def privacy(request):
    return HttpResponse('This is the privacy statement')
