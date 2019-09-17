import pyotp
import requests
import base64
import json
import sys, inspect
from os.path import dirname, join, abspath
from urllib import parse

# os.environ['S3_KEY'] using heroku's environ

# TODO connect duo model to use DB

def _activation_url(qr_url):
	#--- Create request URL
	try:
		data = parse.unquote(qr_url.split('?value=')[1])           # get ?value=XXX
		code = data.split('-')[0].replace('duo://', '')            # first half of value is the activation code
		hostb64 = data.split('-')[1]                               # second half of value is the hostname in base64
		host = base64.b64decode(hostb64 + '='*(-len(hostb64) % 4)) # Same as "api-e4c9863e.duosecurity.com"
		activation_url = 'https://{host}/push/v2/activation/{code}'.format(host=host.decode("utf-8"), code=code) # this api is not publicly known
		print(activation_url)
	except IndexError:
		raise RuntimeError("QR URL is not in proper format.")
	else:
		return activation_url

def _activate(activation_url):
	'''Activates through activation url and returns HOTP key '''
	#--- Get response which will be a JSON of secret keys, customer names, etc.
	#--- Expected Response: {'response': {'hotp_secret': 'blahblah123', ...}, 'stat': 'OK'}
	#--- Expected Error: {'code': 40403, 'message': 'Unknown activation code', 'stat': 'FAIL'}
	try:
		response = requests.post(activation_url)
		response_dict = json.loads(response.text)
		print(response_dict)
		if response_dict['stat'] == 'FAIL':
			raise Exception("The given URL is invalid. Try a new QR/Activation URL")
		hotp_secret = response_dict['response']['hotp_secret']
		return hotp_secret
	except ConnectionError as e:
		raise e
	except KeyError:
		raise Exception("Response is in unexpected format: {}".format(response.text))


def activate(qr_url):
	activation_url = _activation_url(qr_url)
	hotp_secret = _activate(activation_url)
	return hotp_secret

def encode(hotp_secret):
	encoded_secret = base64.b32encode(hotp_secret.encode("utf-8"))
	return encoded_secret

def generate_hotp(hotp_secret, current_at=0, n=1):
	'''Generate `n` number of HOTPs starting at the `current_at` count
	using `hotp_secret` that looks like `7e1c0372fec015ac976765ef4bb5c3f3`'''
	#--- Create HOTP object
	encoded_secret = encode(hotp_secret)
	hotp = pyotp.HOTP(encoded_secret)   # As long as the secret key is the same, the HOTP object is the same

	#--- Generate new passcode
	passcode_list = []
	for i in range(n):
		passcode = hotp.at(current_at + i)
		passcode_list.append(passcode)
	return passcode_list






