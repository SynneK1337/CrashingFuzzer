import fbchat
import configparser

# Parsing the config file
config = configparser.ConfigParser()
config.read('config.cfg')
login = config['LOGIN']['email']
psw = config['LOGIN']['pass']
victim = config['OPTIONS']['victim_id']
print(psw)
# Loging into FB
client = fbchat.Client(login, psw)
