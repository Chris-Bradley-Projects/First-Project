import socket 

HEADER = 64 # Used for telling the server how many bytes will be in the message from the client. The 64 bytes is a buffer that is recived first. You need to make sure the legth of this message is long enough to represent the length of the messgae coming from the client
PORT = 5050
SERVER_IP = "10.0.2.15"
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT" # We need a disconnect message so that we can cleanly disconnect the client from the server

ADDR = (SERVER_IP, PORT) # We need to bind the IP and Port togther to establish the connection

# AUTO_SERVER_IP = socket.gethostbyname(socket.gethostbyname()) # This is a way of automatically getting the local IPV4 adress. Not working right now

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # The client will now connect to the same port
client.connect(ADDR) # Connecting to the IP and Port specified

def send(msg):

    message = msg.encode(FORMAT) # we need to encode the message in UTF-8 format
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
