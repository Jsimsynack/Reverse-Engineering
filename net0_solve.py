#!/bin/python3


import pwn,subprocess,sys,struct


host = '127.0.0.1'
port = '2999'
pid = 0

# Running the vulnerable target program to get the daemon started
r = subprocess.run(['./net0'])


######### Uncomment this section if you want to attach it to gdb #########

# Running 'ps -aux' to grab find the PID of the orphaned process
#ps = subprocess.run(['ps','-aux'],capture_output=True,text=True,universal_newlines=True)

# Cleaning up output from 'ps -aux'
#output = ps.stdout.split('\n')

# Grabbing the PID and adding it to our pid variable
#for line in output:
#	if './net0' in line:
#		pid += int(line.split()[1])

# Attaching gdb to the PID assigned to the daemon process via it's PID
#remote = pwn.gdb.attach(pid)

######### Uncomment this section if you want to attach it to gdb #########


with pwn.remote(host,int(port)) as a:
	
	# Printing the header
	line_one = a.recvline().decode()
	print('\n' + str(line_one))
	
	# Isolating the interger for conversion
	number = int(line_one.split()[2].strip("'"))
	
	# Converting the interger to a 32-bit, little endian byte string
	new_line = struct.pack('I',number)
	print(f'Sending back: {new_line}\n')
	
	# Sending over the new byte string
	a.send(new_line)
	
	reply = a.recvline().decode()
	if 'Thank you' in reply:
		print(reply)
	else:
		print('You are an asbolute failure!')


