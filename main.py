import fbchat
import configparser
import time
import random
# Parsing the config file
config = configparser.ConfigParser()
config.read('config.cfg')
login = config['LOGIN']['email']
psw = config['LOGIN']['pass']
victim = config['OPTIONS']['victim_id']

# Loging into FB
client = fbchat.Client(login, psw)

# Send a message
random.seed()
for i in range(0, 1114112):
  try:
    client.sendMessage(chr(i), victim)
  except:
    print(time.ctime(), i, chr(i), "failed.")

  else:
    print(time.ctime(), i, chr(i), " successful")

  time.sleep(random.random*3)