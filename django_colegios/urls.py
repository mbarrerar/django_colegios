from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView,DetailView,CreateView,DeleteView
from colegios.views import index,ColegioDetailView,ColegioCreateView,ColegioDeleteView
from django.conf import settings
from django.conf.urls.static import static
from login import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',RedirectView.as_view(url='/accounts/login')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^colegios/$', index.as_view(), name='colegios.index'),
    url(r'^accounts/logout/$', views.logout_view, name="login.logout"),
    url(r'^accounts/login/$', views.auth_login, name="login.login"),
    url(r'^colegio/detail/(?P<pk>[0-9]+)/$',ColegioDetailView.as_view(),name="colegios.detail"),
    url(r'^colegio/create/$',ColegioCreateView.as_view(),name="colegios.create"),
    url(r'^colegio/delete/(?P<pk>[0-9]+)/$',ColegioDeleteView.as_view(),name="colegios.delete"),

   
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


