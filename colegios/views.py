from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from braces.views import LoginRequiredMixin
from colegios.models import Colegios
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
from inspector_panel import debug
from colegios.forms import ColegioForm
from django.core.urlresolvers import reverse_lazy
from core.views import MessageMixin

class index(LoginRequiredMixin,ListView):
	model = Colegios
	template_name = 'colegios/index.html'
	paginate_by = 30
	context_object_name = 'colegio_list'
	"""queryset = Colegios.relacionados.filter()"""


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


class ColegioCreateView(LoginRequiredMixin,CreateView):
	model = Colegios
	template_name = 'colegios/create.html'
	success_url = '/colegios/'
	form_class= ColegioForm


class ColegioDeleteView(MessageMixin,LoginRequiredMixin,DeleteView):
        model = Colegios
        success_url = '/colegios/'
	success_message = 'Prueba'
	

class ColegioDetailView(LoginRequiredMixin,DetailView):
	model = Colegios
	template_name = 'colegios/detail.html'
	
	def get_ip(self):
		debug(self.request)
		return self.request.META['REMOTE_ADDR']
	def get_time(self,**kwargs):
		return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

	def get_context_data(self, **kwargs):
		context = super(ColegioDetailView, self).get_context_data(**kwargs)
		context['date'] = self.get_time()
		context['ip'] = self.get_ip()
		return context





      
	
