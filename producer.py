import requests
import json
from requests.auth import HTTPBasicAuth
import sys

x = requests.get("http://192.168.0.106:8111/app/rest/builds/buildTypeId:"+sys.argv[1]+"/status",auth = HTTPBasicAuth('admin','admin'))
print(x.text)
print("Hello")
