from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.shortcuts import redirect
from django.http import HttpResponse


class ContactPageView(CreateView):
	model = Contact
	template_name='contact.html'
	fields = ('name', 'email', 'message')

	def form_valid(self, form):
		return super().form_valid(form)

