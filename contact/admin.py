from django.contrib import admin
from .models import Contact

class AdminSite(admin.ModelAdmin):
	list_display = ("name", "email", "message")

admin.site.register(Contact, AdminSite)
