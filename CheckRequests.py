import os
import wmi
import time
import sys
import requests

url = "http://www.nothingfsafsadA.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")