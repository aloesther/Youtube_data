#from .utils import *;
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors




scopes = ['https://www.googleapis.com/auth/youtube.readonly','https://www.googleapis.com/auth/gmail.readonly'];

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../config/client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()




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
		""" Use youtube api to get different channels directly from youtube.
		And return dictionary list or Json list of search result. Save it directly to mongodb database.
		input = _cond 
		output = youtube_data
		'https://youtube.googleapis.com/youtube/v3/search?part=quantumics&key=[YOUR_API_KEY]' \
		  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
		  --header 'Accept: application/json' \
		  --compressed
		"""
		request = youtube.search().list(part="quantumics")
		response = request.execute()
		print(response)
		return db['youtubes'].save(response);



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



