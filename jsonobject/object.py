#!/bin/python
import json
import sys
path = sys.argv[1]
print(path)

with open(path) as f:
  data = json.load(f)
#res = json.loads(str1)
key_list = []
def printDict(d,key):
    for k, v in d.items():
key_list.append(k)
if type(v) is dict:
printDict(v,key)
else:
if key in key_list:
print(v)
else:
print('No key found')

ip = input('enter key\n')
printDict(data,ip)
