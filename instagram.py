from instagrapi import Client
from main import main


# Replace 'username' and 'password' with your Instagram username and password
cl = Client()
cl.login('juan_sir9', 'juanerc')

# Replace 'userid' with the Instagram user ID of the person you want to message
cl.direct_send('OK', 'text', [userid])
