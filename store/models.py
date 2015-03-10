from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)

    def __string__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __string__(self):
        return self.tag
    

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Album, blank=True)
    ident = models.CharField(max_length=60, blank=True, null=True) #id for image
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    status = models.BooleanField(default=True)  # True is unsold
    user = models.ForeignKey(User, null=True, blank=True)

    def __string__(self):
        return self.image.name

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['title','price','status']
    list_display = ['title']


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']


class ImageAdmin(admin.ModelAdmin):
    search_fields = ['title', 'price', 'ident', 'status']
    list_display = ['__string__', 'title', 'user', 'ident', 'status', 'created']
    list_filter = ['tags']
