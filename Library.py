# Library- Array
import array 
arr= array.array('i',[1,2,3,4])
print(arr)

#Random
import random
print(random.randint(1,10))
print(random.choice(['apple','cherry']))

#file and directory Access
'''import os
print(os.getcwd())
os.mkdir('test_dir')'''

#High level operation on files and collection of files
import shutil
shutil.copyfile('source.txt','designation.txt')

#Data serialization
import json
data={'name':'shruti','age':21}

json_str=json.dumps(data)
print(json_str)

print(json.loads(json_str))


#CSV
import csv
with open('example.csv',made='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
with open('example.csv',mode='r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#Datetime
from datetime import datetime, timedelta

now= datetime.now()
print(now)

yesterday=now - timedelta(days=1)
print(yesterday)

#time
import time
print(time.time())
time.sleep(2)
print(time.time())

#regular expression
import re
pattern=r'\dt'
text='there are 123 apples'
match=re.search(pattern,text)
print(match.group())