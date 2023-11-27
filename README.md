# Part 1

This is my code for the first part of the assignment 3 of CS301 course (Computer Networks). This is the implementation of `ssh` utilising native sockets provided by Python.  
This project requires `python>=3.0` and works using all the native packages only except the `psutils` package just for the Welcome Message to the client. 

To run the code:
- Open the files and update the `sname` and `sport` variable with the Machine IPv4 address and your desired and free Port. If on a single machine, let it remain as it is, it will be operating over localhost and over port 8000.
- Open a terminal and run `python3 serverssh.py`.
- Open another terminal and run `python3 clientssh.py`
- It will ask for the username and password which are by default: `username: server` and `password: 1234`. You may modify these if required at the `python3 serverssh.py` file.  

Remember the order of running the python files matters and the `serverssh.py` should be run first.
