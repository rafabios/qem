
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.template import RequestContext
from .handle_tvshow import retrieve_tvshow, retrieve_episode, load_api_json, is_empty, check_json
import os , json 
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#from .forms import NameForm, Login, AccForm, AccFormDep
#from .models import Usuario, Conta, Dependente, DependenteConta
from .models import TvShowModel, TvShowEpModel
#from django.contrib.auth import authenticate, login as auth_login

#from django.contrib.auth import logout
#from django.contrib.auth.models import User
### temp 2 ####

def teste(request):
	return render(request,'webapp/ajax.html')

def lista(request):
	
	if request.is_ajax:
		search=request.GET.get('start','')

		tvshow=TvShowModel.objects.filter(tvs_name__icontains=search)

		results=[]
		for tv in tvshow:
			tv_json={}
			tv_json['label']=tv.tvs_name
			tv_json['value']=tv.tvs_name
			results.append(tv_json)

		data_json=json.dumps(results[:5])

	else:
		data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)





#### temp ###
from dal import autocomplete  #temp-test

from django.core.urlresolvers import reverse_lazy
from django.views.generic import  UpdateView

from .forms import TvShowForm
#from select2_many_to_many.models import TestModel


class TvAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        #if not self.request.user.is_authenticated():
        #    return Doctor.objects.none()

        qs = TvShowModel.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

class TvShowForm(autocomplete.FutureModelForm):
	class Meta:
	    model = TvShowModel
	    fields = ('tvs_name',)
	    widgets = {
	        'TvShowModel': autocomplete.ModelSelect2(url='select2_outside_admin')
	    }


class sss(UpdateView):
    model = TvShowModel
    form_class = TvShowForm
    template_name = 'webapp/select2_outside_admin.html'
    success_url = reverse_lazy('select2_outside_admin')

    def get_object(self):
        return TvShowModel.objects.first()


### temp ###


def index(request):

	return render(request, 'webapp/base.html')

def showlist(request):
	
	list_to_db = []
	open_json = os.listdir('webapp/')
	
	# Function for Saving json data to the TVSHowModel database #

	def db_handle(value):
		def db_save(j):
			db_save_ = TvShowModel(
			tvs_id = j['id'],
			tvs_name =  j['name'],
			tvs_name_br = "",
			tvs_genre = j['genres'],
			tvs_language = j['language'],
			tvs_status = j['status'],
			tvs_runtime = j['runtime'],
			tvs_schedule = j['schedule']['days'],
			tvs_rating = j['rating']['average'],
			tvs_timezone = "",
			tvs_imdb_id = j['externals']['imdb'],
			tvs_img_m_url = j['image']['medium'],
			tvs_summary = j['summary'],
			tvs_summary_br = "",
			tvs_likes = '1',	
			)	
			db_save_.save()
			#print(j['image']['medium'])
		try:
			print(j['id'])
			j['image']['medium']
		except TypeError:
			j['image'] = {'medium': 'assets/img/tvshow_na.jpg'}
			db_save(value)
		else:	
			db_save(value)
			
	# End of Function #				


	# Loop in order to open the json file and a loop for the json list #
	
	# Use only for populate all the data into the database!!!!! #

	'''
	for n in open_json:
		if 'json' in n:
			list_to_db.append(n)

	for l in list_to_db:
		j_file = open('webapp/'+l, "r")
		j_data = json.load(j_file)

		for j in j_data:

			db_handle(j)
					
	'''
	# End of Loop #		

	# Episode retrieve and Function block #
	def db_ep_handle(value,tvs_id):

		def db_save(tve,tvs_id):				
			db_ep_save = TvShowEpModel(
			tvshowmodel = tvs_id, 
			tve_name  = tve['name'],
			tve_season = tve['season'],
			tve_ep_number = tve['number'],
			tve_airdate = tve['airdate'],
			tve_airtime = tve['airtime'],
			tve_img_ep  = tve['image']['medium'],
			tve_runtime = tve['runtime'],
			tve_summary = tve['summary'],
			tve_summary_br = "",
			)
			db_ep_save.save()
		try:
			#print(tve)
			#tve['image']
			db_save(value,tvs_id)
		except :
			tve['image'] = {'medium': 'assets/img/tvshowep_na.jpg'}
			db_save(value,tvs_id)
		else:	
			#db_save(value,tvs_id)
			pass

	# Episode retrieve End block #		

	# Query tv show block #


	if request.method == 'GET':
		
		tvshow_get = request.GET['tvshowname']	
		print(tvshow_get)


		#return render(request, 'page.html' {'data' : query_res }) #Usar
		#print(query_req.meta_id())
		query_req = TvShowModel.objects.get(tvs_name__iexact=tvshow_get)
		query_res = query_req.meta_info()
		dir(query_res)
		query_id = query_req.meta_id()
		try:
			q_ep = TvShowEpModel.objects.get(tvshowmodel_id=int(query_id))
			print(q_ep)
			#q_ep = TvShowEpModel.objects.filter(tvshowmodel_id=69) #worked
		except ObjectDoesNotExist:
			print("except")
			json_data_ep = retrieve_episode(query_id)
			for tve in json_data_ep:
				#print(tve)
				db_ep_handle(tve,query_req)
				#return render(request, 'page.html' {'data' : query_res, 'data_ep': q_ep })
				#data_ep = []
				#data_ep = TvShowEpModel.objects.filter(tvshowmodel_id=int(query_id)).meta_info()

		except MultipleObjectsReturned:
			data_ep = []
			data_ep = TvShowEpModel.objects.filter(tvshowmodel_id=int(query_id))	
				
		else:
			data_ep = []
			data_ep = TvShowEpModel.objects.filter(tvshowmodel_id=int(query_id)).meta_info()	

		#data_ep = []
		#data_ep = TvShowEpModel.objects.filter(tvshowmodel_id=int(query_id)).meta_info()


		data_seasons = []
		data_s = TvShowEpModel.objects.filter(tvshowmodel_id=int(query_id)).values('tve_season')
		#print(dir(data_s))
		for x in data_s:	
			#print(x)
			data_seasons.append(x['tve_season'])
			#print (type(data_seasons))
			b = list(set(data_seasons))
			#print(b)
			 	
			#print(data_sc)
		#data_sc = b.sort()	
		#print(data_sc)
		#'data_seasons' : data_sc 
		return render(request, 'webapp/add_tvshow.html', {'data' : query_req, 'data_ep': data_ep, 'data_seasons' : b })
		
	
	

	# Query tv show block #


	#tv_show_query = TvShowModel()
	#aaa = TvShowModel.objects.all().filter(tvs_id='178')	
	#aaa = TvShowModel.objects.filter(tvs_name__icontains='The Walking Dead')
	#aaa = TvShowModel.objects.get(tvs_name__iexact='The BlackList')
	#aaa = TvShowModel.objects.get(query_req.meta_info())
	
	#for x in aaa.meta_info():
	#for x in aaa:

		#print(x.meta_info())
		#print(aaa.meta_info())

	#return HttpResponse(x.meta_info())	





	return HttpResponse(query_req.meta_info())


def search(request):

	return render(request, 'webapp/search.html')

