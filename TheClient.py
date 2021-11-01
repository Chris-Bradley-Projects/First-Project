import socket 
import time

HEADER = 64 # Used for telling the server how many bytes will be in the message from the client. The 64 bytes is a buffer that is recived first. You need to make sure the legth of this message is long enough to represent the length of the messgae coming from the client
PORT = 5050
SERVER_IP = "10.0.2.15"
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT" # We need a disconnect message so that we can cleanly disconnect the client from the server

ADDR = (SERVER_IP, PORT) # We need to bind the IP and Port togther to establish the connection

# AUTO_SERVER_IP = socket.gethostbyname(socket.gethostbyname()) # This is a way of automatically getting the local IPV4 adress. Not working right now

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # The client will now connect to the same port

try:
    client.connect(ADDR) # Connecting to the IP and Port specified
except:
    ADDR = (SERVER_IP, (PORT + 1))
    client.connect(ADDR)


def messageLength(message):

    keep_sending_message = True
    
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # turn the length of the message about to be sent into a string and then encode it in utf-8
    send_length += (b'' * (HEADER - len(send_length))) # not sure why we need this but keeping it just in case
    #print(send_length)

    while keep_sending_message == True:

        client.send(send_length) # send the length of the message first 
    
        message_reponse = client.recv(2048).decode(FORMAT)

        if message_reponse == "Message Failed":
            keep_sending_message = True
        elif message_reponse == "Message Success":
            keep_sending_message = False
        else:
            pass
    
    return send_length

def send(msg):
    
    message = msg.encode(FORMAT) # we need to encode the message in UTF-8 format
    
    message_length = messageLength(message)
    print(message_length)
    
    client.send(message) # send the message
    

send("Hello World!")
input()
send("Love the world")
input()
send(DISCONNECT_MESSAGE)
