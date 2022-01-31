import requests
import json
from requests.auth import HTTPBasicAuth
import sys

status = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/status",auth = HTTPBasicAuth('admin','admin'))
startTime = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/startDate",auth = HTTPBasicAuth('admin','admin'))
endTime = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/finishDate",auth = HTTPBasicAuth('admin','admin'))
print(status.text)
print(startTime.text)
print(endTime.text)
print("Hello")
