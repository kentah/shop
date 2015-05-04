from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import admin


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
    

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='media')
    tags = models.ManyToManyField(Tag, blank=True)
    ident = models.CharField(max_length=60, blank=True, null=True) #id for image
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    status = models.BooleanField(default=True)  # True is unsold
    user = models.ForeignKey(User, null=True, blank=True)

    def thumb(self):    # to display thumbnail in admin
        thumbnail = '<img src="%s" width="100" height="100" />' % (self.image)
        return thumbnail
    thumb.allow_tags = True

    def scarf_sort(self):
        x = self.image
        for s in x.filter(tags='scarf'):
            self.scarf = s
        return self.scarf

    def __str__(self):
        return self.image.name


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']


class ImageAdmin(admin.ModelAdmin):

    search_fields = ['title', 'price', 'ident', 'status']
    list_display = ['__str__', 'thumb', 'title', 'user', 'ident', 'status', 'created']
    list_filter = ['tags']


class JoinForm(models.Model):
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)


class JoinAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
