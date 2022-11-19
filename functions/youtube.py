#from .utils import *;
import googleapiclient.discovery

# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyCYHVvZSGo08mVk5j_Epwf8wuJWDyOOWzk"
# API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
# 'request' variable is the only thing you must change
# depending on the resource and method you need to use
# in your query


def create(self):
	return self.save();



def save(self, youtubedt):
	return db['youtubes'].save(youtubedt);



def read(self, _cond):
	return db['youtubes'].get(_cond if _cond else None);



def get(self, _cond):
	return self.read(_cond);



def list(self, _cond):
	return self.read(_cond);



def update(self, _cond, youtubedt):
	return db['youtubes'].update(_cond, youtubedt);



def edit(self, _cond, youtubedt):
	return self.update(_cond, youtubedt);



def delete(self, _cond):
	return db['youtubes'].remove(_cond);



def export(self, _cond):
	return migrateMongoDB2CSV('youtubes', _cond);



def extract(self, _cond):
	""" Use youtube api to get different channels directly from youtube.
	And return dictionary list or Json list of search result. Save it directly to mongodb database.
	input = _cond 
	output = youtube_data
	'https://youtube.googleapis.com/youtube/v3/search?part=quantumics&key=[YOUR_API_KEY]' \
	  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
	  --header 'Accept: application/json' \
	  --compressed
	"""
	request = youtube.search(**_cond).list(part='snippet');
	response = request.execute()
	#db['youtubes'].save(response);
	return response



def transform(self, _cond, youtubedt):
	""" Use analytics and data science methods to filter channels that match prospects conditions
	the search results given in the _cond
	input = (_cond, youtube_data )
	output = prospect_data """
	def f():
		pass
	def g():
		pass
	return g(f(youtubedt));



def load(self, prospectdt):
	""" Save this in the prospect database"""
	return db['prospects'].save(prospectdt);





