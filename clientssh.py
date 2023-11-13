from socket import *
import sys

sname="127.0.0.1"
sport=8000

csock=socket(AF_INET,SOCK_STREAM)
csock.connect((sname,sport))

while(True):
    usrname=input("Enter the server username: ")
    csock.send(usrname.encode())
    susr_res=csock.recv(2048)
    print(susr_res)
    if(susr_res.decode()=='1'):
        while(True):
            passwd=input("Enter the server password: ")
            csock.send(passwd.encode())
            spass_res=csock.recv(2048)
            if(spass_res.decode()=='1'):
                print(f"You have now been connected to @{usrname}")
                break
            else:
                print("The password you entered is wrong. Please try again.")
        break
    else:
        print("The given username does not exist, please try again.")

welcome_message=csock.recv(2048)
print(welcome_message.decode())
cmd=input("Enter any UNIX command (ls,pwd,cd,echo etc). Enter 'exit' to close the connection: ")

while cmd!="exit":
    csock.send(cmd.encode())
    cont=csock.recv(2048)
    print(cont.decode())

    cmd=input("Enter another UNIX command.Enter 'exit' to close the connection: ")
    if cmd=="exit":
        break
csock.close()

if(cmd=="exit"):
    csock.close()
    sys.exit()