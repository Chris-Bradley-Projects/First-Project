import socket 
import threading

HEADER = 64 # Used for telling the server how many bytes will be in the message from the client. The 64 bytes is a buffer that is recived first. You need to make sure the legth of this message is long enough to represent the length of the messgae coming from the client
PORT = 5050
SERVER_IP = "10.0.2.15"
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT" # We need a disconnect message so that we can cleanly disconnect the client from the server

ADDR = (SERVER_IP, PORT) # We need to bind the IP and Port togther to establish the connection

# AUTO_SERVER_IP = socket.gethostbyname(socket.gethostbyname()) # This is a way of automatically getting the local IPV4 adress. Not working right now


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # Binding the IP and port 


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # This will decode the bytes into a string in the utf-8 format. We are returing the length of the message that the client is about to send
        msg_length = int(msg_length) # convert to an interger
        msg = conn.recv(msg_length).decode(FORMAT) # Now that we know the length of the message about to be sent we can actually recive the message and then decode it to a string
        
        if msg == DISCONNECT_MESSAGE: 
            connected = False # we are setting connected equal to False if the msg from the server is equal to the DISSCONNECT_MESSAGE  
        
        print(f"[{addr}] {msg}")

    conn.close() # If connected is set to True then we want to close the connection



def start():
    server.listen() # listening for new connections to the IP and Port
    print("Server is listening on " + "" + SERVER_IP ) 
    while True:
        conn, addr = server.accept() # We establish the connection and the reurn value is conn and addr. conn is the connection adn addr is the IP of the Device connecting
        thread = threading.Thread(target=handle_client, args=(conn,addr)) # Here we are running each clients connection a a seprate thread and we are passing the arguments to our handle_client function. It is important for them to be on a seprate thread so that when we wait for a message from a client it does not disrupt a differnt client from sending a message. 
        thread.start() # We start the new thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # Here threading.activeCount returns the amount of thread running but we subtract 1 becasue the start() function is running and that does not count as a connectionS

print("Server is starting....")
start()