'''
I.
    Use 17.2 socket to play with the program
    Make accept more than one connection successively
    Terminate connection on ctrl+D or 'quit' input
    ??? program hangs

II.
    openssl command -> connect to Google over https
    $ openssl s_client -connect google.com:443
    ??? verify error:num=20:unable to get local issuer certificate

III.
    Decrypt ROT13: http://rot13.com/index.php
        Gel gur ffy_pyvrag pbzznaq. -> Try the ssl_client command
        Hfr gur -pbaarpg bcgvba. -> Use the -connect option
'''
import socket

TCP_IP = '0.0.0.0'  # This means that we should bind to all the addresses your computer has
TCP_PORT = 5005  # Port we're listening on
BUFFER_SIZE = 20  # In bytes, how many bytes to wait for before recv returns

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # It's an Internet socket, and it's a stream
s.bind((TCP_IP, TCP_PORT))  # bind the socket to the IP + port
s.listen(1)  # start listening on that socket
conn, addr = s.accept()  # Accept a connection from the socket

print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print "received data:", data
    conn.send(data)
conn.close()
