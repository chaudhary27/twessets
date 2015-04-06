import os
import csv
import random
import string
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
script, filename = argv

f = open(filename, 'w')


def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	return file_path

path = get_file_path('tw.csv')


def read_csv(file_path):
	array_tw_handle = []
	with open(file_path, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			array_tw_handle.extend(row)
	return array_tw_handle


array_tw_handle = read_csv(path)

handles = array_tw_handle

def twitter_handle(handle):
	url = "http://twitter.com/"+handle
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	#[x['src'] for x in soup.findAll('img', {'class': 'sizedProdImage'})]
	#LOGO_IMG = soup.find_all("img", {"class": "ProfileAvatar-image"})
	#soup.findAll('img')[0].get('src')
	LOGO_IMG = [x['src'] for x in soup.findAll('img', {'class': 'ProfileAvatar-image'})]
	#LOGO_IMG = soup.findAll('img', {'class': 'ProfileAvatar-image'}).get('src')
	BG_IMG = soup.find_all("div", {"class": "ProfileCanopy-headerBg"})
	#BG_IMG = [x['img'] for x in soup.findAll('div', {'class': 'ProfileCanopy-headerBg'})]
	return {'LOGO_URL>>':LOGO_IMG, 'BG_IMG_URL>>':BG_IMG}
	

assets = []
for twHandle in handles:
	assets = twitter_handle(twHandle)
	f.write(str(assets))

f.close()

