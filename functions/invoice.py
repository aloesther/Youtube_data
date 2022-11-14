from .utils import *;





class InvoiceHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



	def create(self):
		pass



	def save(self, invoicedt):
		return db['invoices'].save(invoicedt);



	def read(self, _cond):
		return db['invoices'].list(_cond);



	def get(self, _cond):
		return self.read(_cond);



	def list(self, _cond):
		return self.read(_cond);



	def update(self, _cond, invoicedt):
		return db['invoices'].update(_cond, invoicedt)



	def edit(self, _cond, invoicedt):
		return self.update(_cond, invoicedt);



	def delete(self, _cond):
		return db['invoices'].remove(_cond);


	def export(self, _cond):
		return migrateMongoDB2CSV('invoices', _cond);



	def forwardToPayment(self):
		pass



	def confirmPayment(self):
		pass

