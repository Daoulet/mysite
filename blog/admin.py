from django.contrib import admin
from .models import Post

class AdminSite(admin.ModelAdmin):
	list_display = ("title", "author", "published_date")

admin.site.register(Post, AdminSite)
# Register your models here.
