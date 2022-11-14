from .utils import *;
from pyyoutube import Api



ytapi = Api(api_key="your api key")




class YouTubeHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



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
		youtubedt = ytapi.search(_cond);
		return db['youtubes'].save(youtubedt);



	def transform(self, _cond, youtubedt):
		def f():
			pass
		def g():
			pass
		return g(f(youtubedt));



	def load(self, prospectdt):
		return db['prospects'].save(prospectdt);



