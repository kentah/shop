from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.utils import timezone

from .models import Image, JoinForm, Tag
from .forms import Join


def index(request):
    msg = 'This is the main page'
    context = {'msg': msg}
    return render(request, 'store/index.html', context)

def shop(request):
    #scarf = Image.objects.all()
    #image2 = Image.objects.get(trying and failing to get image field)
    scarf = Image.objects.filter(tags=2)  #2scarf 3bowl 4decor 5gallery 6sold
    bowl = Image.objects.filter(tags=3)
    decor = Image.objects.filter(tags=4)
    #gallery = Image.objects.filter(tags=5)
    context = {'scarf': scarf,
               'bowl': bowl,
               'decor': decor,
               }           
    return render(request, 'store/shop.html', context) 

def shop_detail(request):
     
    msg = 'hey'
    return render(request, 'store/shop_detail.html', {'msg': msg})


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

    
@login_required(redirect_field_name='sign_in')
def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to success page
        else:
            msg = 'Disabled account'
    else:
        msg = 'Invalid login'

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

#the below may work when clicking on an image and creating a page
"""
class ShopView(DetailView):

    model = Image

    def shop_detail(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
"""
