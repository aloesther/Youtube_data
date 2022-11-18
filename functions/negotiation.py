from __future__ import print_function
#from .utils import *;
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
        	flow = InstalledAppFlow.from_client_secrets_file('./client_secret.json', SCOPES, redirect_uri='http://localhost:3003/callback');
        	creds = flow.run_local_server(port=3003);
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()




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



