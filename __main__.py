from apis import youtube;
from flask import Flask;
app = Flask(__name__);


youtube._init_(app);
dataformat._init_(app);


def init(_cond):
	"""1. Team Member 1 creates a shortlist of prospective talent on a spreadsheet and shares it with Team Member 2. Shortlist may be based on certain criteria needed for an upcoming campaign
   		1. E.g. 300K-1M average views, Gaming
		2. Team Member 2 goes through the list and picks the ones that are relevant
		3. Team Member 1 develops unique first lines for each prospect and adds to spreadsheet
		4. Team Member 1 adds the final list to a Mavros Master List spreadsheet, which is our current talent database 
		5. Team Member 2 reviews again and edits if necessary, following which they download the spreadsheet as a .csv file, import into our email campaign management system on https://mailshake.com 
		6. Team Member 2 goes through the process of running the campaign on the system, which is linked to his email address teammember2@mavrosdigital.com, and receives responses to his inbox
		7. Team Member 2 individually liaises with talent/management and negotiates deals via email and updates an external spreadsheet to track responses and status of negotiations 
		8. Team Member 2 adds prospects to shared external spreadsheet with Client, who confirm which of the prospects they are interested in and provide offers
		9. Team Member 2 continues liaising with client partners and talent during negotiation and updates them on status of prospects
		10. Once agreed upon, Team Member 2/3 manages the delivery of the service, including contracts, briefs, final product etc. being sent via email
		11. Team Member 3 follows up on invoicing and payments to wrap up
	"""
	yt.load(yt.tranform(yt.extract(_cond)));
	pr.load(pr.generateBio(pr.list()));
	ms.sendCampaign(ms.createCampaign());
	ng.startMonitor();


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)