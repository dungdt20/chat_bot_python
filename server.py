# first of all import the socket library 
import socket     
from _thread import *
from queue import Queue 

s = socket.socket()          
print ("Socket successfully created")

port = 12345                
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
s.listen(5)      
print ("socket is listening")
list_of_clients = []

def multi_threaded_client(conn, addr):
    conn.send(("Welcome to this chatroom!").encode())

    while 1:
        try:
            data = conn.recv(2048)
            msg = data.decode('utf-8')
            if msg:
                print ("<", addr[1], "> ", msg) 
                # Calls broadcast function to send message to all 
                message_to_send = msg 
                broadcast((message_to_send).encode(), conn) 
            else: 
                remove(conn) 
 
        except: 
            continue

    
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

# a forever loop until we interrupt it or  
# an error occurs 
threadCount = 0
while 1: 
    # Establish connection with client. 
    conn, addr = s.accept()      
    print('Got connection from', addr)
    list_of_clients.append(conn)
    start_new_thread(multi_threaded_client, (conn, addr))
    threadCount += 1
    print('Thread Number: ' + str(threadCount))