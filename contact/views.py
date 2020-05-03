from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Contact
from django.shortcuts import redirect
from django.http import HttpResponse


class SendSuccess(TemplateView):
	template_name = 'sended.html'

class ContactPageView(CreateView):
	model = Contact
	template_name='contact.html'
	fields = ('name', 'email', 'message')

	def form_valid(self, form):
		return super().form_valid(form)

