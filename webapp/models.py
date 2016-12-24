from django.db import models

# Create your models here.

class TvShowModel(models.Model):

	tvs_id = models.IntegerField(primary_key=True)
	tvs_name = models.CharField(max_length=100)
	tvs_name_br = models.CharField(max_length=100, blank=True,default="")
	tvs_genre = models.CharField(max_length=100, blank=True,default="", null=True)
	tvs_language = models.CharField(max_length=100,  blank=True,default="", null=True)
	tvs_status = models.CharField(max_length=100, null=True)
	tvs_runtime = models.FloatField(blank=True,default="", null=True)
	tvs_schedule = models.CharField(max_length=100,  blank=True,default="", null=True)
	tvs_rating = models.CharField(max_length=100, blank=True,default="", null=True)
	tvs_timezone = models.CharField(max_length=100, blank=True,default="", null=True)
	tvs_imdb_id = models.CharField(max_length=100, null=True, blank=True,default="")
	tvs_img_m_url = models.CharField(max_length=100, null=True, blank=True,default="")
	tvs_summary = models.TextField(max_length=100, null=True, blank=True,default="")
	tvs_summary_br = models.TextField(max_length=100, null=True, blank=True,default="")
	tvs_likes = models.FloatField()


	def __str__(self):
		return self.tvs_name 
		'''
		return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self, 
			self.tvs_id, 
			self.tvs_name, 
			self.tvs_genre,
			self.tvs_status, 
			self.tvs_runtime, 
			self.tvs_rating, 
			self.tvs_img_m_url,
			self.tvs_summary)
		'''
	def meta_info(self):

		return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format(self, 
			self.tvs_id, 
			self.tvs_name,
			self.tvs_name_br, 
			self.tvs_genre,
			self.tvs_language,
			self.tvs_status, 
			self.tvs_runtime, 
			self.tvs_schedule,
			self.tvs_rating, 
			self.tvs_img_m_url,
			self.tvs_summary,
			self.tvs_summary_br)	

	def meta_id(self):	

		string = str(self.tvs_id)
		return string



class TvShowEpModel(models.Model):

	tvshowmodel = models.ForeignKey(TvShowModel, on_delete=models.CASCADE)
	tve_name = models.CharField(max_length=100)
	tve_season = models.IntegerField()
	tve_ep_number = models.IntegerField()
	tve_airdate = models.CharField(max_length=100)
	tve_airtime = models.CharField(max_length=100)
	tve_img_ep = models.CharField(max_length=100)
	tve_runtime = models.FloatField()
	tve_summary = models.TextField(max_length=400)
	tve_summary_br = models.TextField(max_length=400,  blank=True,default="")

	def __str__(self):
		return self.tvshowmodel

	def meta_info(self):

		return "{0} {1} {2} {3} {4} {5} {6} {7} {8}".format(self, 
			self.tve_name,
			self.tve_season,
			self.tve_ep_number,
			self.tve_airdate,
			self.tve_airtime,
			self.tve_img_ep,
			self.tve_runtime,
			self.tve_summary,
			self.tve_summary_br)

	def meta_season(self):
	
		return self.tve_season


class TVLikes(models.Model):

	likes_tvshow = models.ForeignKey(TvShowModel, on_delete=models.CASCADE )
	likes_episode = models.ForeignKey(TvShowEpModel, on_delete=models.CASCADE )
	user = models.CharField(max_length=100)
	likes_n = models.IntegerField()
