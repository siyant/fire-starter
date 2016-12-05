import requests
import csv

url = # firebase json url, eg. 'https://projectname.firebaseio.com/shoppinglist.json'
file = # path to CSV file, eg. 'csvtest.csv'

reader = csv.reader(open(file))
info = ''
csvheaders = []

for row in reader:
  if info == '':
    info += '{'
    for header in row:
      csvheaders.append(header)
  else:
    line = '"'+row[0]+'":{'
    for i in range(1,len(csvheaders)):
      line += '"{}":'.format(csvheaders[i])
      if not row[i].isdigit():
        row[i] = '"'+row[i]+'"'
      line += '{},'.format(row[i])
    info += line[0:-1]+'},'
info = info[0:-1]+'}'
r = requests.patch(url, data = info)
print (r.text)