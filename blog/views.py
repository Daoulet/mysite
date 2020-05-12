from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import Q

class HomePageView(ListView):
	model = Post
	template_name='home.html'

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name='post_detail_view.html'


class SearchResultsView(ListView):
	model = Post
	context_object_name = 'post'
	template_name='search_results.html'
	
	def get_queryset(self):
		query = self.request.GET.get('q')
		return Post.objects.filter(
			Q(title__icontains=query) | Q (title__icontains=query)
		)
	
