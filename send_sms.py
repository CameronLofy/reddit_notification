from twilio.rest import Client
from config import twilio_account, twilio_auth, twilio_nums, user_num

client = Client(twilio_account, twilio_auth)

def send_sms(message):
    for num in twilio_nums:
        client.messages.create(to= num,
                               from_= user_num,
                               body= message)
        print("Text sent to " +num)
