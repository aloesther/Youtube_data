from utils import *;



#class MasterlistHandler():



def __new__(self):
	pass



def __init__(self):
	pass



def create(self):
	pass



def save(self, masterlistdt):
	return db['masterlists'].insert_many(masterlistdt);



def read(self, _cond):
	return db['masterlists'].find(_cond);



def get(self, _cond):
	return self.read(_cond);



def list(self, _cond):
	return self.read(_cond);



def update(self, _cond, masterlistdt):
	return db['masterlists'].update(_cond, masterlistdt)



def edit(self, _cond, masterlistdt):
	return self.update(_cond, masterlistdt);



def delete(self, _cond):
	return db['masterlists'].remove(_cond);


def importD(self, _cond):
	return migrateCSVMongoDB('masterlists', _cond);


def exportD(self, _cond):
	return migrateMongoDB2CSV('masterlists', _cond);


def generateBioUpdate(self, _cond, _biocond):
	return db['masterlists'].update(_cond, self.generateBio(_biocond));



def generateBio(self, _cond):
	gen = pipeline();
	return gen(_cond);



def generateCampaign(self, _cond):
	gen = pipeline();
	return gen(_cond);



def sendCampaign(self, _cond, messages):
	mailer = SMTPMailer()
	messages = []
	email_msg = EmailMessage(messages, _cond.frm, _cond.to)
	messages.append(email_msg)
	response=mailer.send_messages(*messages)
	def transform(_cond):
		pass
	def startNegotiation(_cond):
		db['negotiations'].save(transform(_cond))
	startNegotiation(_cond);
	return response;



