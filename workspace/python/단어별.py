import csv


L = []

file = open("c:/mywork/ibm_기적20분.txt", encoding='utf8')

while(1):
    line = file.read().replace(' ','').replace(' ','').replace(' ','').replace('.','').replace(',','')

    try: escape = line.index('\n')
    except: escape = len(line)

    if line:
        L.append(line[0:escape])
    else:
        break

f = open("C:/mywork/"+"ibm_기적20분"+".csv", 'w', newline='', encoding='utf8')

with f:

    writer = csv.writer(f)
    for row in L:
        
        writer.writerow(row)
f.close()

print(L)