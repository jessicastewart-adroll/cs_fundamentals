'''
Server program that accepts multiple connections.

TODO:
Write program that connects to this one.
Sends string to this program, then quits.
Will see log in stdout.
Bonus: Send string as command line argument.
'''
import socket
TCP_IP = '0.0.0.0'  # This means that we should bind to all the addresses your computer has
TCP_PORT = 5005  # Port we're listening on
BUFFER_SIZE = 20  # In bytes, how many bytes to wait for before recv returns
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # It's an Internet socket, and it's a stream
s.bind((TCP_IP, TCP_PORT))  # bind the socket to the IP + port
s.listen(2)  # start listening on that socket, let 2 clients wait in the queue before refusing connections
while 1:
    conn, addr = s.accept()  # Accept a connection from the socket
    while 1:
        data = conn.recv(BUFFER_SIZE) # wait for data of 20 bytes or more.
        if not data:
            break
        if "quit" in data:
            break
        print "received data: ", data
        conn.send(data)
    conn.close()
