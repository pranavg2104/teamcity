import requests
import json
from requests.auth import HTTPBasicAuth
import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer


def kafkaProducer(feature,start,end,duration,status):

    kafkaServer = 'kafka.vhil-dev.kpit.com:9092'

    producer = KafkaProducer(
        bootstrap_servers=kafkaServer,
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    data = {'Feature': feature, 'Build_Status': status , 'Start_Time':start,'End_Time':end,'Total_Duration':duration}
    producer.send('stla', value=data)


if __name__ == "__main__":
  status = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/status",auth = HTTPBasicAuth('admin','admin'))
  startTime = sys.argv[2]
  endTime = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/finishDate",auth = HTTPBasicAuth('admin','admin'))
  #print(status.text)
  finishTime = endTime.text[9:15:1]
  duration = requests.get("http://192.168.0.106:8111/app/rest/builds/buildType:"+sys.argv[1]+"/statistics/BuildDuration",auth = HTTPBasicAuth('admin','admin'))
  startTime = startTime[:2] + ':' + startTime[2:4] + ':' + startTime[4:] 
  #print(startTime)
  finishTime = finishTime[:2] + ':' + finishTime[2:4] + ':' + finishTime[4:] 
  #print(finishTime)
  #print(int(duration.text)/(1000*3600))
  kafkaProducer(sys.argv[1],startTime,finishTime,int(duration.text)/(1000*3600),status.text)




