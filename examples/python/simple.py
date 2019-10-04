#!/usr/bin/env python3
import urllib3
import xml.etree.ElementTree as ET





#Download xml
http = urllib3.PoolManager()
r = http.request(
     'POST',
     'http://localhost:8080/read.php',
     fields={
            'user': 'fabio',
            'pass': 'secret',
            'sql' : 'select * from contacts'
     })
if (r.status==200):
    #print(r.data)
    xml=r.data
else:
    print("Error on connection...")
    exit()


#Parse xml
root = ET.fromstring(xml)

#Check for error
if root.tag=="error":
    print("Error: %s" % root.text)
    exit()


#print column names
ncol=0
for fields in root.iter('field'):
    print("|%s|" % fields.attrib['name'],end='')
    ncol+= 1

print("")

#print row content
currCell=0
for record in root.findall('./records/record/cell'):
    currCell+=1
    print("|%s|" % record.text,end='')
    if (currCell==ncol):
         print()
         currCell=0
