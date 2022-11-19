#from .utils import *;
import googleapiclient.discovery

# API information
api_service_name = "gmail"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyCYHVvZSGo08mVk5j_Epwf8wuJWDyOOWzk"
# API client
gmail = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
# 'request' variable is the only thing you must change
# depending on the resource and method you need to use
# in your query




#class NegotiationHandler():



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
	request = gmail.search();
	# Query execution
	response = request.execute()
	# Print the results
	print(response)
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



