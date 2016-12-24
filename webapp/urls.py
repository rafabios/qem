from django.conf.urls import url
from . import views
from django.http import HttpResponse
from .views import UpdateView



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^showlist', views.showlist, name='showlist'),
	url(r'^search', views.search, name='search'),
    url(r'^sss',views.TvAutocomplete.as_view(),name='select2_outside_admin'),
    url(r'^ajax/$',views.lista),
    url(r'^teste/$',views.teste),
		]