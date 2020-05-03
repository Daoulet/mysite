from django.urls import path
from .views import ContactPageView, SendSuccess


urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('contact/success/', SendSuccess.as_view(),name='success'),
]