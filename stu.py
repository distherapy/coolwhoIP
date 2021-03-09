import socket
import whois
import json
from urllib.request import urlopen

ratchet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ratchet.bind((socket.gethostname(), 80))
#get_ip = request.environ['REMOTE_ADDR']  
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
ip=data['ip']
w = whois.whois('ip')

def whoip():
  pass

whoip()
print(ip, w)

