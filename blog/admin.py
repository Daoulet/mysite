from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
	model = Comment

#  StackedInline
class AdminSite(admin.ModelAdmin):
	list_display = ("title", "author", "published_date")
	inlines = [
		CommentInline,
	]

admin.site.register(Post, AdminSite)
admin.site.register(Comment)

# Register your models here.