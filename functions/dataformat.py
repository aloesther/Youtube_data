from .utils import *;


class MasterlistHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



	def create(self):
		pass



	def save(self, dataformatdt):
		return db['dataformats'].save(dataformatdt);



	def read(self, _cond):
		return db['dataformats'].list(_cond);



	def get(self, _cond):
		return self.read(_cond);



	def list(self, _cond):
		return self.read(_cond);



	def update(self, _cond, dataformatdt):
		return db['dataformats'].update(_cond, dataformatdt)



	def edit(self, _cond, dataformatdt):
		return self.update(_cond, dataformatdt);



	def delete(self, _cond):
		return db['dataformats'].remove(_cond);


	def export(self, _cond):
		return migrateMongoDB2CSV('dataformats', _cond);


