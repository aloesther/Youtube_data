from .utils import *;


class ProspectHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



	def create(self):
		pass



	def save(self, prospectdt):
		return db['prospects'].save(prospectdt);



	def read(self, _cond):
		return db['prospects'].get(_cond);



	def get(self, _cond):
		return self.read(_cond);



	def list(self):
		return self.read(_cond);



	def edit(self, _cond, prospectdt):
		return self.update(_cond, prospectdt);



	def update(self, _cond, prospectdt):
		return db['prospects'].update(_cond, prospectdt);




	def delete(self, _cond):
		return db['prospects'].delete(_cond);




	def load(self, _cond):
		def transform(youtubedt):
			pass
		return db['masterlists'].save(transform(prospectdt));



	def export(self, _cond):
		return migrateMongoDB2CSV(_cond);



