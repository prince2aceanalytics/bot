from datetime import datetime
from db import insert_into_db

class WhatsApp:
   def __init__(self, rqst):	
        self.request = rqst
        
   def message_extractor(self):
       incoming_no = self.request.values.get('From','')
       now = datetime.now()
       date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
       receiver_no = self.request.values.get('To','')
       incoming_msg = self.request.values.get('Body', '').lower()
       account_sid=self.request.values.get('AccountSid', '')
       api_version=self.request.values.get('ApiVersion')
       message_sid=self.request.values.get('MessageSid')
       num_segments=self.request.values.get('NumSegments')
       num_media=self.request.values.get('NumMedia')
       sms_message_sid=self.request.values.get('MessageSid')
       sms_sid=self.request.values.get('SmsSid')
       numMedia = self.request.values.get('NumMedia')
       smsstatus = self.request.values.get('SmsStatus')
       insertion_date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
       insert_into_db(incoming_no,receiver_no,incoming_msg,incoming_msg,date_time,account_sid,message_sid,num_segments, numMedia,smsstatus,insertion_date_time)

       return incoming_no, receiver_no, incoming_msg, date_time, numMedia
