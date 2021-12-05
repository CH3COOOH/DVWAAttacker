import requests as rq
import sys
import json

with open(sys.argv[2], 'r') as o:
    _json = o.read()

header_insert = {}
param_insert = {}

if sys.argv[1] == '-h':
    header_insert = json.loads(_json)
elif sys.argv[1] == '-p':
    param_insert = json.loads(_json)

s = rq.Session()
s.headers.update(header_insert)

r = s.get('http://172.20.1.251/login.php', params=param_insert)

# print(s.headers)
for k in s.headers.keys():
    print('%s: %s' % (k, s.headers[k]))
print(r.url)
