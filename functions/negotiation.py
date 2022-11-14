from .utils import *;




class NegotiationHandler():



	def __new__(self):
		pass



	def __init__(self):
		pass



	def create(self):
		pass



	def save(self, negotiationdt):
		return db['negotiations'].save(negotiationdt);



	def read(self, _cond):
		return db['negotiations'].list(_cond);



	def get(self, _cond):
		return self.read(_cond);



	def list(self, _cond):
		return self.read(_cond);



	def update(self, _cond, negotiationdt):
		return db['negotiations'].update(_cond, negotiationdt)



	def edit(self, _cond, negotiationdt):
		return self.update(_cond, negotiationdt);



	def delete(self, _cond):
		return db['negotiations'].remove(_cond);


	def export(self, _cond):
		return migrateMongoDB2CSV('negotiations', _cond);



	def monitor(self, _cond):
		# This is a monitoring service function/app
		pass



	def generateResponse(self, _cond):
		gen = pipeline();
		return gen(_cond);



	def respond(self, _cond, messages):
		mailer = SMTPMailer()
		messages = []
		email_msg = EmailMessage(messages, _cond.frm, _cond.to)
		messages.append(email_msg)
		response=mailer.send_messages(*messages)
		db['negotiations'].update(_cond, messages);
		return response;



