import os
import subprocess
from socket import *
import psutil
from datetime import datetime


sname="127.0.0.1"
sport=8000

ssocket=socket(AF_INET,SOCK_STREAM)
ssocket.bind((sname,sport))
ssocket.listen(10)

username="server"
password="1234"
last_login_list=[]

while(1):
    connsocket,addr=ssocket.accept()
    print(addr)
    while(True):
        cl_usrname=connsocket.recv(2048)
        if(cl_usrname.decode()==username):
            connsocket.send("1".encode())
            while(True):
                cl_passwd=connsocket.recv(2048)
                if(cl_passwd.decode()==password):
                    connsocket.send("1".encode())
                    break
                else:
                    connsocket.send('0'.decode())
            break
        else:
            connsocket.send('0'.decode())

    memory_info = psutil.virtual_memory()
    mem_use_per=memory_info.percent

    process_list = psutil.process_iter()
    num_processes = len(list(process_list))

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    first=False
    
    last_login_list[cl_usrname.decode()].append(formatted_datetime)
    if(len(last_login_list)==1):
        last_login="This is your first time logging into this host."
    else:
        last_login=last_login_list[-2]

    welcome_message=f"""
    Welcome to {username}
    Memory Usage: {mem_use_per}%
    Processes: {num_processes}
    IPv4 Address: {sname}
    Last Login: {last_login}"""

    connsocket.send(welcome_message.encode())

    while(True):
        cl_cmd=connsocket.recv(2048)
        cmd=cl_cmd.decode()

        if(cmd=="exit"):
            connsocket.close()
            break
        if(cmd[0:2]=='cd'):
            folder=cmd[cmd.index(" ")+1:]
            if(folder==".."):
                os.chdir("..")
            else:
                os.chdir(os.path.join(os.getcwd(),folder))
            print_result = subprocess.run(['pwd'], shell=True, stdout=subprocess.PIPE, text=True)
            connsocket.send((f'Changed directories. Currently at {print_result.stdout}').encode())
        elif(cmd[0:5]=='mkdir'):
            result = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE, text=True)
            connsocket.send(f'Directory {cmd[6:]} has been created.'.encode())
        else:
            result = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE, text=True)
            connsocket.send(result.stdout.encode())

    connsocket.close()
ssocket.close()