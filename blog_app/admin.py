from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    # 管理界面显示
    list_display = ('title', 'id', 'tags',  'date')
    # 排序方式 -号表示降序
    ordering = ('-date',)
    # 搜索字段
    search_fields = ('title', 'date', 'tags', 'id')
    # 筛选
    list_filter = ['date']


admin.site.register(Blog, BlogAdmin)









