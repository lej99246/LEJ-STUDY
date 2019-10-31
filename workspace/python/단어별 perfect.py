import csv

transcript = ''
with open("c:/mywork/dae81.txt", encoding='utf8') as f0:
    transcript = f0.read()
    #print(f0.read())

#transcript = open("c:/파일비교/"+"대기업8정답"+".txt",'rb').readline().decode('utf-8')

f = open("C:/mywork/"+"dae8ans"+".csv", 'w', newline='', encoding='utf8')

csvWriter = csv.writer(f)

all = []
for row in transcript:
    all.append(row)
csvWriter.writerow(all)

f.close()