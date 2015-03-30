from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Image, JoinForm
from .forms import Join

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

    ####################  figure out image display  ##################


def shop(request):
    image = Image()
    msg = 'This is the shopping page'
    context = {'image': image.image, 'title': image.title }           
    return render(request, 'store/shop.html', context)

def join(request):
    #context = RequestContext(request)

    if request.method == 'POST':
        form = Join(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = Join()

    return render(request, 'store/join.html', {'form': form})

def sign_in(request):
    msg = 'This is where users log in'
    context = {'msg': msg}
    return render(request, 'store/sign_in.html', context)

def terms(request):
    return HttpResponse('This displays the terms of the site')

def privacy(request):
    return HttpResponse('This is the privacy statement')

def cart(request):
    msg = 'This is where you view your cart, obviously'
    context = {'msg': msg}
    return render(request, 'store/cart.html', context)
