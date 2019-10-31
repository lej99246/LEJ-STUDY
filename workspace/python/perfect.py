import base64

import urllib.request
import urllib.parse

import json

import csv

import ast
import timeit

 

url = 'https://brain.deepgram.com/v2/listen?model=general&language=ko'

username = 'jm.lee@masonai.kr'

password = 'dlwlals'

 

headers = {}

headers['Authorization'] = 'Basic {}'.format(

  base64.b64encode('{}:{}'.format(username, password).encode('utf-8')).decode('utf-8')

)

 

headers['Content-Type'] = 'audio/wav'

start = timeit.default_timer()

#data_open = open('C:/파일비교/'+'샘플비디오'+'.vob', 'rb') # 로컬 파일위치
#data_open = open('C:/파일비교/'+'샘플비디오'+'.mp4', 'rb') # 로컬 파일위치
#data_open = open('C:/파일비교/'+'기적의수면법_20분'+'.mp3', 'rb')
data_open = open('C:/파일비교/'+'골프존'+'.m4a', 'rb')



print("동영상")
req = urllib.request.Request(

  url,

  method='POST',

  headers=headers,

  data=data_open

)

resp = urllib.request.urlopen(req)

result = resp.read().decode('utf-8')

print("123")

data = ast.literal_eval(result)

 

transcript = data.get('results').get('channels')[0].get('alternatives')[0].get('transcript').replace(' ','').replace(' ','').replace(' ','')

confidence = data.get('results').get('channels')[0].get('alternatives')[0].get('confidence')

 
print(transcript)
f = open("C:/동영상엑셀/"+"골프존필드"+".csv", 'w', newline='')

csvWriter = csv.writer(f)

all = []
for row in transcript:
    all.append(row)
csvWriter.writerow(all)

f.close()

end = timeit.default_timer()
print(end - start)

print(confidence)

f.close()