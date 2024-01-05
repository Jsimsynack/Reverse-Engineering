#/usr/bin/python3

import socket,struct,sys

host = '127.0.0.1'
port = 2997

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    total = 0
    s.connect((host,port))

  # Grabbing each 4 byte string being sent over the wire consecutively
    l1 = s.recv(4)
    l2 = s.recv(4)
    l3 = s.recv(4)
    l4 = s.recv(4)

  # Unpacking each byte string into integers
    dec_l1 = struct.unpack("<I",l1)[0]
    dec_l2 = struct.unpack("<I",l2)[0]
    dec_l3 = struct.unpack("<I",l3)[0]
    dec_l4 = struct.unpack("<I",l4)[0]

# Adding all of the integers together
    total += dec_l1 + dec_l2 + dec_l3 + dec_l4

    print(f'[+] Total: {total}')

# Making sure that the integer does not overflow 32-bit packing maximum
    if total <= 4294967295:

# Packing our total and sending back over the wire 
        packed_total = struct.pack("I",total)
        s.send(packed_total)
        reply = s.recv(1024).decode()
        print(reply)
      
    else:
        print('''
[+] Struct cannot pack integer larger than: 4294967295 (0xffffffff)
[+] Just keep running it until you are successful!!''')
        sys.exit()
