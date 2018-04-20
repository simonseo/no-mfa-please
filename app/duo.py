import pyotp
import requests
import base64
import json
import sys, inspect
from os.path import dirname, join, abspath
from urllib import parse

# os.environ['S3_KEY'] using heroku's environ


def _activation_url(qr_url):
	#--- Create request URL
	data = parse.unquote(qr_url.split('?value=')[1])           # get ?value=XXX
	code = data.split('-')[0].replace('duo://', '')            # first half of value is the activation code
	hostb64 = data.split('-')[1]                               # second half of value is the hostname in base64
	host = base64.b64decode(hostb64 + '='*(-len(hostb64) % 4)) # Same as "api-e4c9863e.duosecurity.com"
	activation_url = 'https://{host}/push/v2/activation/{code}'.format(host=host.decode("utf-8"), code=code) # this api is not publicly known
	print(activation_url)
	return activation_url

def _activate(activation_url):
	'''Activates through activation url and returns HOTP key '''
	#--- Get response which will be a JSON of secret keys, customer names, etc.
	#--- Expected Response: {'response': {'hotp_secret': 'blahblah123', ...}, 'stat': 'OK'}
	#--- Expected Error: {'code': 40403, 'message': 'Unknown activation code', 'stat': 'FAIL'}
	response = requests.post(activation_url)
	response_dict = json.loads(response.text)
	if response_dict['stat'] == 'FAIL':
		raise Exception("The given URL is invalid. Try a new QR/Activation URL")
	print(response_dict)

	hotp_secret = response_dict['response']['hotp_secret']
	return hotp_secret

def activate(qr_url):
	activation_url = _activation_url(qr_url)
	hotp_secret = _activate(activation_url)
	return hotp_secret

def encode(hotp_secret):
	encoded_secret = base64.b32encode(hotp_secret.encode("utf-8"))
	return encoded_secret

def save_secret(hotp_secret, count):
	'''Save updated info to DB
	hotp_secret should look like "7e1c0372fec015ac976765ef4bb5c3f3" 
	count should be an int'''
	secrets = {
		"hotp_secret" : hotp_secret,
		"count" : count
	}
	with open(SECRETFILE, "w") as f:
		json.dump(secrets, f)

def load_secret():
	'''loads datarow from DB'''
	try:
		with open(SECRETFILE, "r") as f:
			secret_dict = json.load(f)
	except Exception as e:
		raise
	return secret_dict


def HOTP(hotp_secret, count=0):
	'''Usage: generate = HOTP(); passcode = generate()'''
	#--- Create HOTP object
	encoded_secret = encode(hotp_secret)
	HOTP.hotp = pyotp.HOTP(encoded_secret)   # As long as the secret key is the same, the HOTP object is the same
	HOTP.count = count

	#--- Generate new passcode
	def generate(n=1):
		passcode_list = []
		for i in range(n):
			passcode = HOTP.hotp.at(HOTP.count + i)
			passcode_list.append(passcode)
		save_secret(hotp_secret, HOTP.count + n)
		return passcode_list
	return generate






