import requests

x = requests.get("http://localhost:8111/app/rest/builds/buildType:Teamcity_Build/status")
print(x.status_code)
print("Hello")
