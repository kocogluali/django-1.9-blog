from django.contrib import admin

from Blog.models import Post, Category, AboutAndContact


# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_filter = ['title', 'category']
    list_display = ['title', 'updated', 'published']
    search_fields = ['title', 'content', 'user']


class AdminCategory(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name']
    search_fields = ['name']


class AdminAboutAndContact(admin.ModelAdmin):
    list_display = ['__unicode__']


admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(AboutAndContact,AdminAboutAndContact)
