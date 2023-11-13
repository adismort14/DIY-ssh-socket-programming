import os
import subprocess
from socket import *


sname="10.10.64.179"
sport=8080

ssocket=socket(AF_INET,SOCK_STREAM)
ssocket.bind((sname,sport))
ssocket.listen(10)

username="adismort"
password="1234"

while(1):
    connsocket,addr=ssocket.accept()
    while(True):
        cl_usrname=connsocket.recv(2048)
        if(cl_usrname.decode()=='adismort'):
            connsocket.send("1".encode())
            while(True):
                cl_passwd=connsocket.recv(2048)
                if(cl_passwd.decode()=='1234'):
                    connsocket.send("1".encode())
                    break
                else:
                    connsocket.send('0'.decode())
            break
        else:
            connsocket.send('0'.decode())

    while(True):
        cl_cmd=connsocket.recv(2048)
        cmd=cl_cmd.decode()

        if(cmd=="exit"):
            break
        result = subprocess.run([cmd], stdout=subprocess.PIPE, text=True)
        connsocket.send(result.stdout.encode())

    connsocket.close()
ssocket.close()