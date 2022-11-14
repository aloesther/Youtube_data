from .utils import *;




class DealHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



	def create(self):
		pass



	def save(self, dealdt):
		return db['deals'].save(dealdt);



	def read(self, _cond):
		return db['deals'].list(_cond);



	def get(self, _cond):
		return self.read(_cond);



	def list(self, _cond):
		return self.read(_cond);



	def update(self, _cond, dealdt):
		return db['deals'].update(_cond, dealdt)



	def edit(self, _cond, dealdt):
		return self.update(_cond, dealdt);



	def delete(self, _cond):
		return db['deals'].remove(_cond);


	def export(self, _cond):
		return migrateMongoDB2CSV('deals', _cond);



	def getClient(self, _cond):
		return self.read(_cond);



	def getTalent(self):
		return self.read(_cond);



	def sendDeal(self, _cond):
		mailer = SMTPMailer()
		messages = []
		email_msg = EmailMessage(messages, _cond.frm, _cond.to)
		messages.append(email_msg)
		response=mailer.send_messages(*messages)
		db['deals'].update(_cond, messages);
		return response;


	def confirmDeal(self, _cond):
		return self.update(_cond, {'confirm':1});



