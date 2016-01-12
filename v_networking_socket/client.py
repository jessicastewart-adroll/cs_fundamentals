import socket
import sys

DEFAULT_MESSAGE = "This is a string to send to Paul's server."

client_socket = socket.create_connection(('0.0.0.0', 5005))

try:
    message = " ".join(sys.argv[1:]) if sys.argv[1:] else DEFAULT_MESSAGE
    print "Sending {}".format(message)
    client_socket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client_socket.recv(20)
        amount_received += len(data)
        print "Received {}".format(data)
finally:
    print "Closing socket."
    client_socket.close()