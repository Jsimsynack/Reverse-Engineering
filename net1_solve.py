#!/bin/python3


import subprocess,struct,socket


host = '127.0.0.1'
port = 2998

# Running the vulnerable target program to get the daemon started
r = subprocess.run(['./net1'])

		
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((host,port))
	random = s.recv(1024)
	temp.write(random)

# This will unpack the random 4 bytes into an integer
	rev_bytes = struct.unpack('<I',random)[0]
	print(f'Unpacked String:\n{rev_bytes}')
	
	print(f'Sending....')

# Sending back a string representation of the unpacked integer from above
	s.send(bytes(str(rev_bytes),'utf-8'))

	output = s.recv(100)
	print(output)

# Terminating the daemon
e = subprocess.run(['killall','net1'])
print('All cleaned up!')
