from django.contrib import admin
from .models import Picture
# Register your models here.


class PictureAdmin(admin.ModelAdmin):
    fields = ['title', 'date', 'description', 'image', ]
    list_display = ('title', 'id',  'date', )

    ordering = ('-date', )

    search_fields = ('id', 'title', 'date', )

    list_filter = ['date']


admin.site.register(Picture, PictureAdmin)