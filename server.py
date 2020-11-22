import socket
import sys

def create_socket():
    try:
        global host 
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as err:
        print(f"Error creating socket: {err}")

# Bind the socket to the port and host
def bind_socket():
    try:
        global host
        global port
        global s

        print(f"Binding to port {port}")

        s.bind((host, port))
        s.listen(5)

    except socket.error as err:
        print(f"Error binding socket: {err}\nRetrying...")
        bind_socket()

# Accept communication from the client (socket must be bound and listening)
def accept():
    # try:
    global s
    conn, address = s.accept()
    print(f"Connection has been established! Ip: {address[0]}, Port: {address[1]}")
    # send_command(conn)
    conn.close()