from flask import Flask, request
import requests
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
import model
#import chat_file
from chat_log import WhatsApp
#from chatflow
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
   wa_obj = WhatsApp(rqst=request)
   resp = MessagingResponse()
   msg = resp.message()
   incoming_no, receiver_no, incoming_msg, date_time, numMedia = wa_obj.message_extractor()
   response = model.response_function(incoming_msg)
   #response  = str("From: "+ incoming_no + " To: " + receiver_no + " Message:" + incoming_msg + " " +date_time + " Num_Media: "+ numMedia)
   msg.body(response)
   return str(resp)
   
"""
@app.route('/chat_log', methods=['POST'])   
def chat_log():
   resp_chat = request.get_data()
   return resp_chat
   
"""
	

if __name__ == '__main__':
   app.run()