from twilio.rest import TwilioRestClient
from msms_config import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER
import argparse
import time

parser = argparse.ArgumentParser(description="Send a mass text")
parser.add_argument("--message", "-m",  type=str, help="Message to send")
parser.add_argument("--phonebook", "-p", type=open, help="File to read numbers from", default="numbers.txt")

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def send_to_phonebook(phonebook_f, msg_txt):
    for line in phonebook_f:
        number = line.strip()
        if number[0] != "+":
            number = "+1{}".format(number)
 

        message = client.messages.create(
                    body=msg_txt,
                    to=number,    # Replace with your phone number
                    from_=FROM_NUMBER) # Replace with your Twilio number
        print number, message.sid, msg_txt
        time.sleep(0.5)

if __name__ == "__main__":
    args = parser.parse_args()
    send_to_phonebook(args.phonebook, args.message)
