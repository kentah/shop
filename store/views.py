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
    scarf = Image.objects.filter(tags=2)  #2scarf 3bowl 4decor 5gallery 6sold
    bowl = Image.objects.filter(tags=3)
    decor = Image.objects.filter(tags=4)
    #gallery = Image.objects.filter(tags=5)
    context = {'scarf': scarf,
               'bowl': bowl,
               'decor': decor,
               }
   
    return render(request, 'store/shop.html', context) 


def shop_detail(request, id):

    product = Image.objects.get(id=id)
    image = product.image
    price = product.price
    title = product.title
    description = product.description
    slug = product.slug
    tags = product.tags
    created = product.created
    context = {'product': product,
               'title': title,
               'image': image,
               'description': description,
               'price': price,
               'tags': tags,
               'created': created
           }
    return render(request, 'store/shop_detail.html', context)

def cart(request):
    msg = 'This is where you view your cart, obviously'
    context = {'msg': msg}
    return render(request, 'store/cart.html', context)

#the below may work when clicking on an image and creating a page
'''
class ShopView(DetailView):

    model = Image

    def shop(self):
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

    def shop_detail(self):
        img = get_object_or_404(Image, id=id)
        msg = 'hey'
        return render(request, 'store/shop_detail.html', {'msg':msg})
'''


def terms(request):
    return HttpResponse('''
    <h2>WEBSITE TERMS AND CONDITIONS</h2>
    '''
    )

def privacy(request):
    return HttpResponse('This is the privacy statement')
