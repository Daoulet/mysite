from django.urls import path
from . import views
from .views import HomePageView, PostDetailView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]