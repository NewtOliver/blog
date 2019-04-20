from django.contrib import admin
from .models import Account
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'password', 'date']
    list_display = ('name', 'email', 'password', 'date')

    ordering = ('-date', )

    search_fields = ('id', 'email', 'date', )

    list_filter = ['date']


admin.site.register(Account, AccountAdmin)