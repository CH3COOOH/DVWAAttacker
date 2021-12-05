#  Simulate login action, with 2 fail patterns
# Usage: python3 login-dvwa.py <counrs> <1 | 0 (different | same username)>

import requests as rq
from lxml import html
import sys

ctr = int(sys.argv[1])
dic = int(sys.argv[2])

s = rq.Session()
r = s.get('http://172.20.1.251/login.php')

header_insert = {
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://172.20.1.251',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://172.20.1.251/login.php'
        }

s.headers.update(header_insert)
print(s.headers)

for i in range(ctr):
    tree = html.fromstring(r.text)
    token = tree.xpath('//input[@name="user_token"]/@value')
    
    username = 'admin'
    password = 'pwd_' + str(i)
    if dic == 1:
        username += str(i)
    try:
        r = s.post('http://172.20.1.251/login.php', data='username=%s&password=%s&Login=Login&user_token=%s' % (username, password, token[0]))
        print('No.%d try with (%s, %s), token=%s' % (i+1, username, password, token[0]))
    except:
        print('~~~~~~~~\n' + r.text + '\n~~~~~~~~')
        print('^^ Responsed changed. No token can be found.')
        break

    if 'Login failed' in r.text:
        print('Login failed')
