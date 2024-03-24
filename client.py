# Import socket module 
import socket
from _thread import *


# Create a socket object 
s = socket.socket()          

# Define the port on which you want to connect 
port = 12345                

# connect to the server on local computer 
s.connect(('', port)) 
res = s.recv(2048)
print ("[CLIENT]: ", res.decode('utf-8'))
# msg = input("Enter your name: ")
# s.send(str.encode(msg))
# print ("[CLIENT]: ", s.recv(2048).decode('utf-8'))

def handle_recv_msg(conn: socket.socket):
    while 1:
        try:
            new_msg = (s.recv(2048).decode('utf-8'))
            print (new_msg)        
        except Exception as e:
            print(f'Error handling message from server: {e}')
            conn.close()
            break

while 1:
    start_new_thread(handle_recv_msg, (s,))
    msg = input()
    if msg == "":
        continue
    if msg == "quit":
        s.close()
        break
    s.send((msg).encode())