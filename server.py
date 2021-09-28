import threading
import socket
import webbrowser
import datetime as dt
import youtube_test


import youtube_test

IP = '127.0.0.1'
port = 59000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # first for IPv4 the secound for tcp protocol
server_socket.bind((IP, port))  # to commnicate with the port
server_socket.listen()
clients = []
dev = []

def send_all(msg):
    for client in clients:
        client.send(msg)


def recive_messge(client):
    while True:
        try:
            message = client.recv(1024)
            send_all(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = dev[index]
            send_all('{} has left the chat room!'.format(name).encode('utf-8'))
            dev.remove(name)
            break


def server_connection():
    while True:
        print('Server is running and listening ...')
        client, address = server_socket.accept()
        print('{} Connected'.format(str(address)))
        client.send('test'.encode('utf-8'))
        dev_name = client.recv(1024)
        dev.append(dev_name)
        clients.append(client)
        print('nickname is {}'.format(dev_name).encode('utf-8'))
        send_all('{} has connected to the chat room '.format(dev_name).encode('utf-8'))
        client.send('U R now connected!'.encode('utf-8'))
        thread = threading.Thread(target=recive_messge, args=(client,))
        thread.start()


if __name__ == "__main__":
    server_connection()

# def recive_message(client_socket):
#     try:
#         message_header = client_socket.recv(header_length)
#         if not len(message_header):
#             return False
#
#
#         message_length=int(message_header.decode("utf-8").strip())# remove spaces in the start and the end f the string
#         return{"header":message_header,"data":client_socket.recv(message_length)}
#     except:
#         return False
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# while True:
#     read_sockets,_,exception_sockets=select.select(socket_list,[],socket_list)# read write and error
#     for notified_socket in read_sockets:
#         if notified_socket==server_socket:
#             client_socket,client_address=server_socket.accept()
#
#             user=recive_message(client_socket)
#             if user is False:
#                 continue
#             socket_list.append(client_socket)
#             clients[client_socket]=user
#             print(f"accepted from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
#
#         else:
#             message=recive_message(notified_socket)
#             if message is False:
#                 print(f"closed connetion to{clients[notified_socket]['data'].decode('utf-8')}")
#                 socket_list.remove(notified_socket)
#                 del clients[notified_socket]
#                 continue
#             user=clients[notified_socket]
#             print(f"rececid massege from{user['data'].decode('utf=8')}:{message['data'].decode('ut-8')}")
#             for client_socket in clients:
#                 if client_socket != notified_socket:
#                     client_socket.send(user['header']+user['data']+message['header']+message['data'])
#     for notified_socket in exception_sockets:
#         socket_list.remove(notified_socket)
#         del clients[notified_socket]
