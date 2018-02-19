import fbchat
import configparser
import time
# Parsing the config file
config = configparser.ConfigParser()
config.read('config.cfg')
login = config['LOGIN']['email']
psw = config['LOGIN']['pass']
victim = config['OPTIONS']['victim_id']

# Loging into FB
client = fbchat.Client(login, psw)

# Send a message
for i in range(33, 1114111):
  try:
    client.sendMessage(chr(i), victim)
  except:
    pass