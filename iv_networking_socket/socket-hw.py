'''
I.
    Use 17.2 socket to play with the program
    Make accept more than one connection successively
    Terminate connection on ctrl+C or 'quit' input

    client quit > server keyboard interrupt > create new binding on server: [Errno 48] Address already in use
    list bindings and listeners on port > lsof -i tcp:5005

II.
    openssl command -> connect to Google over https
    $ openssl s_client -connect google.com:443
    verify error:num=20:unable to get local issuer certificate
        CA > certification authority > verifies owner of public keys

III.
    Decrypt ROT13: http://rot13.com/index.php
        Gel gur ffy_pyvrag pbzznaq. -> Try the ssl_client command
        Hfr gur -pbaarpg bcgvba. -> Use the -connect option
'''
import socket
import sys
from thread import start_new_thread

TCP_IP = '0.0.0.0'  # This means that we should bind to all the addresses your computer has
TCP_PORT = 5005  # Port we're listening on
BUFFER_SIZE = 1024  # In bytes, how many bytes to wait for before recv returns

def connection_thread(conn):
    conn.send("Client socket: Welcome! Type something and hit enter\n")
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break

        if data == 'quit\r\n':
            conn.send("Client socket: closing socket.")
            conn.close()
            return
        else:
            reply = "Client socket data: " + data
            conn.sendall(reply)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # It's an Internet socket, and it's a stream
    print "Server socket created."
    s.bind((TCP_IP, TCP_PORT))  # bind the socket to the IP + port
    print "Server socket bind complete."
    s.listen(5)  # start listening on that socket
    print "Server socket listening for up to 5 connections."
    conn = None

    while 1:
        conn, addr = s.accept()  # Accept a connection from the socket
        print "Server socket connected with IP:" + addr[0] + ", port:" + str(addr[1])
        start_new_thread(connection_thread, (conn,))

except KeyboardInterrupt:
    print "Closing server socket and connection through keyboard interrupt"
    if conn:
        conn.close()
    if s:
        s.close()

except Exception as e:
    print "Exception thrown,{}".format(e)
    sys.exit(1)
