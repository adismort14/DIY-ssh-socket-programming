# DIY-ssh-socket-programming

This is my code for the first part of the assignment 3 of CS301 course (Computer Networks). This is the implementation of `ssh` utilising native sockets provided by Python.  
This project has no dependencies except it requires `python>=3.0` and works using all the native packages only.  

To run the code:
- Open the files and update the `sname` variable with the Machine IPv4 address. If on a single machine, let it remain as it is, it will be operating over localhost.
- Open a terminal and run `python3 serverssh.py`.
- Open another terminal and run `python3 clientssh.py`

Remember the order of running the python files matters and the `serverssh.py` should be ran first.
