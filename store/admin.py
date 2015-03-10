from django.contrib import admin

from store.models import Album, AlbumAdmin, Tag, TagAdmin, Image, ImageAdmin

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)

