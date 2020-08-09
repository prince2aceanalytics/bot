from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

import urllib
client = MongoClient("mongodb+srv://talk2prince:"+ urllib.parse.quote("Prince@123")+ "@cluster0-gbasg.mongodb.net/chat_logs?retryWrites=true&w=majority")
db = client.get_database('chat_logs')
records = db.user_data




def insert_into_db(sender_no,receiver_no,incoming_msg,resp_message,datetime,account_sid,message_sid,num_segments,numMedia,smsstatus,insertion_date_time):
    
	new_log = {'from' : sender_no,
				'to' : receiver_no,
				'user_msg' : incoming_msg,
				'resp_message' : resp_message,
				'Date_time' : datetime,
				'account_sid' : account_sid,
				'message_sid' : message_sid,
				'num_segments': num_segments,
				'numMedia' : numMedia,
				'smsstatus' : smsstatus,
				'insertion_date_time' : insertion_date_time
				}
	
	records.insert_one(new_log)
	
	
def reply_node_data(data):
   output = []
   resp_data = db.chat_data_Q_A.find( { "_id": data },{"children": 1, "_id": 0})
   resp_data = str([document["children"] for document in resp_data])
   if resp_data[2:(len(resp_data)-2)] == "":
      return ("Sorry couldn't understand your input")
   else:
      resp_data = resp_data[2:(len(resp_data)-2)]
      return (resp_data)
