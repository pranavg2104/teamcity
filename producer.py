import requests
from requests.auth import HTTPBasicAuth

x = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:Teamcity_Build/status",auth = HTTPBasicAuth('admin','admin'))
print(x)
print("Hello")
