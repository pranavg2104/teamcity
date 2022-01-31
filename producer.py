import requests
import json
from requests.auth import HTTPBasicAuth
import sys

status = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/status",auth = HTTPBasicAuth('admin','admin'))
startTime = sys.argv[2]
endTime = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/finishDate",auth = HTTPBasicAuth('admin','admin'))
print(status.text)
finishTime = endTime.text[9:15:1]
duration = str(int(finishTime) - int(startTime))
duration = duration[:2] + ':' + duration[2:4] + ':' + duration[4:] 

startTime = startTime[:2] + ':' + startTime[2:4] + ':' + startTime[4:] 
print(startTime)
finishTime = finishTime[:2] + ':' + finishTime[2:4] + ':' + finishTime[4:] 
print(finishTime)
print(duration)



