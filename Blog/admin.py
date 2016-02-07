from django.contrib import admin

from Blog.models import Post, Category


# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_filter = ['title','category']
    list_display = ['title','updated', 'published']
    search_fields = ['title', 'content', 'user']


class AdminCategory(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
