from django.contrib import admin
from blog.models import Post, Category


admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Handle display post model in the admin site """
    list_display = ["title", "slug", "status", "author"]
    prepopulate_fields = {"slug":["title"]}
    