import base64

import urllib.request

import urllib.parse

import json

import csv

import ast

 

url = 'https://brain.deepgram.com/v2/listen?model=general&language=ko'

username = 'jm.lee@masonai.kr'

password = 'dlwlals'

 

headers = {}

headers['Authorization'] = 'Basic {}'.format(

  base64.b64encode('{}:{}'.format(username, password).encode('utf-8')).decode('utf-8')

)

 

headers['Content-Type'] = 'audio/wav'

 

data_open = open('C:/인식률비교/'+'광주시'+'.mp3', 'rb') # 로컬 파일위치

 

req = urllib.request.Request(

  url,

  method='POST',

  headers=headers,

  data=data_open

)

resp = urllib.request.urlopen(req)

result = resp.read().decode('utf-8')

 

data = ast.literal_eval(result)

 

transcript = data.get('results').get('channels')[0].get('alternatives')[0].get('transcript').replace(' ','').replace(' ','').replace(' ','')

confidence = data.get('results').get('channels')[0].get('alternatives')[0].get('confidence')

 

f = open("C:/인식률비교/"+"광주시1"+".csv", 'w', newline='')

csvWriter = csv.writer(f)

for row in range(len(transcript)):
    all = []
    all.append(transcript[row])
csvWriter.writerow(all)

f.close()


print(confidence)

f.close()