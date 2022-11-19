import pandas as pd;
import pymongo as pm;
from mailshake import SMTPMailer, EmailMessage;
#from transformers import pipeline



MONGO_DB="mongodb://localhost:27017/";
db = pm.MongoClient(MONGO_DB)['test'];



def getDBDIR(name):
	return '../databases/'+str(name)+'.csv';



def migrateCSV2MongoDB(name, _cond):
	df = pd.read_csv(getDBDIR(name));
	json = df.to_json();
	db[name].insert_many(json);
	return json;



def migrateMongoDB2CSV(name, _cond):
	data=db[name].find({}).cursor();
	csv = pd.read_json(data).to_csv();
	f = open(getDBDIR(name), "a")
	f.write(csv);
	f.close()
	return csv;


