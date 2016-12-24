from sys import argv
import urllib2, urllib, json

#Variables
api_url_path =       "http://api.tvmaze.com/shows"
api_episodes =  "/episodes" # /number/episodes
api_pages =     "?page="  # 500 everypage
file_dir = 		""
last_page = 	"last_page_number" # last id/250




def retrieve_tvshow():
	'''
	try:
   Business Logic here...
except "Invalid level!":
   Exception handling here...
else:
   Rest of the code here...

   except ValueError, Argument:
		print "The argument does not contain numbers\n", Argument	

	'''

	try:

		last_id = open('last_id.txt', 'r')
		idd = last_id.read()
		last_id.close()
		#print "try rodou"
	
	except:
	
		
		#except:	
		#if last_id.read() == "" :
		last_id = open('last_id.txt', 'w+')

		api_url = api_url_path + api_pages + "0"
		#print api_url
		
		tvshow_json = load_api_json(api_url)
		
		file_save = "data_tvshow_pg" + "0" + ".json"
		with open(file_save, 'a') as outfile:
			json.dump(tvshow_json, outfile)

		#file_save = open('tvshow_by_id.json', 'a')
		#file_save.write(tvshow_json)
		#file_save.close()
		
		last_id_tmp = str(tvshow_json[-1]['id'])
		last_id.write(last_id_tmp)
		last_id.close()

		#print "Arquivo Criado e Salvo"
		



	else:

		last_id = open('last_id.txt', 'r+')
		idd = last_id.read()
		#if last_id.read() != '0' :
		#print idd
		tmp_id = int(idd)
		last_id_beg = tmp_id / 249
		last_id_max = last_id_beg + 30
		for x in range(last_id_beg,last_id_max):

			last_id = open('last_id.txt', 'w+')

			api_url = api_url_path + api_pages + str(x)

			tvshow_json = load_api_json(api_url)
			print  api_url
			
			file_save = "data_tvshow_pg" + str(x) + ".json"
			with open(file_save, 'w+') as outfile:
				json.dump(tvshow_json, outfile)		

			#file_save = open('tvshow_by_id.json', 'a')
			#file_save.write(tvshow_json)
			#file_save.close()
		
			last_id_tmp = str(tvshow_json[-1]['id'])
			#print last_id_tmp
			last_id.write(last_id_tmp)
			last_id.close()			
			
			#print "Linhas adicionadas"		

			


	
	
def retrieve_episode(tvshow_id):
	
	n = tvshow_id
	api_url = api_url_path + n + api_episodes
	tvepisodes_json = load_api_json(api_url)

	return tvepisodes_json


def retrieve_episode_file(tvshow_id):
	
	n = tvshow_id
	api_url = api_url_path + n + api_episodes
	tvepisodes_json = load_api_json(api_url)

	file_save = open('tvshow_episodes_by_id.json', 'a')
	file_save.write(tvepisodes_json)
	file_save.close()	


def load_api_json(api_url):
	url = api_url
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	site_api = response.read()
	obj_api = json.loads(site_api)
	return obj_api 		



retrieve_tvshow()	