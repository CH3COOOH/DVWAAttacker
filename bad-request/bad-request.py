import socket
import sys

host = '172.20.1.251'
port = 80
buffer_size = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

with open(sys.argv[1], 'r') as o:
    header = o.read()

header = header.replace('\n', '\r\n')
header = header.replace('NULL', '\0')
print(header.encode('utf-8'))

client.send(header.encode('utf-8'))
res = client.recv(buffer_size)
print(res)
