# importing libraries
import imaplib
import os
from dotenv import load_dotenv 

# read .env file
load_dotenv()
EMAIL_USER = os.environ.get('EMAIL_USER')
PASSWORD = os.environ.get('PASSWORD')
RECIEVED_FROM_EMAIL = os.environ.get('RECIEVED_FROM_EMAIL')
IMAP_URL = os.environ.get('IMAP_URL')
FILENAME = os.environ.get('FILENAME')

# get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
 
# Function to search for a key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
 
# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs

# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(host=IMAP_URL, port=993)

try:
    # logging the user in
    con.login(EMAIL_USER, PASSWORD)
except imaplib.IMAP4.error as e:
    print("[ERROR] Login: %s", e)
    exit(1)

# calling function to check for email under this label
con.select('Inbox')
 
# fetching emails recieved from email: 
msgs = get_emails(search('FROM', RECIEVED_FROM_EMAIL, con))

# open file to write in
absolut_path = os.path.abspath(
    os.path.expanduser(os.path.expandvars('./')))
file = os.path.join(absolut_path, FILENAME)
f = open(file, 'a')

# finding the required content
for msg in msgs:
    if type(msg[0]) is tuple:
        content = str(msg[0][1], 'utf-8').split("YOUR", 1)[-1]
        code = content[397:413]
        print(code)
        f.write(code+"\n")

f.close()
