from dal import autocomplete
from django import forms
from django.forms import extras
from .models import TvShowModel



class TvShowForm(autocomplete.FutureModelForm):
	class Meta:
	    model = TvShowModel
	    fields = ('tvs_name',)
	    widgets = {	'tvshow': autocomplete.ModelSelect2(url='select2_outside_admin', attrs={ 'data-html' : 'true' })}