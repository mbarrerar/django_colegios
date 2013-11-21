from django.shortcuts import render
from django.views.generic import ListView,DetailView
from braces.views import LoginRequiredMixin
from .models import Colegios
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

class index(LoginRequiredMixin,ListView):
	model = Colegios
	template_name = 'colegios/index.html'
	paginate_by = 100
	context_object_name = 'colegio_list'

	def get_context_data(self, **kwargs):
		context = super(index, self).get_context_data(**kwargs)
	        lines = []
	        for i in range(10000):
	            lines.append(u'Line %s' % (i + 1))
	        paginator = Paginator(lines, 10)
	        page = self.request.GET.get('page')
	        try:
	            show_lines = paginator.page(page)
	        except PageNotAnInteger:
	            # If page is not an integer, deliver first page.
	            show_lines = paginator.page(1)
	        except EmptyPage:
	            # If page is out of range (e.g. 9999), deliver last page of results.
	            show_lines = paginator.page(paginator.num_pages)
	        context['lines'] = show_lines
		return context

class detail(LoginRequiredMixin,DetailView):
	model = Colegios
	template_name = 'colegios/detail.html'



      
	
