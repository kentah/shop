from django.contrib import admin

from store.models import Tag, TagAdmin, Image, ImageAdmin, JoinAdmin, JoinForm


admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(JoinForm, JoinAdmin)
