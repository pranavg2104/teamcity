import requests

x = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:Teamcity_Build/status")
print(x)
print("Hello")
