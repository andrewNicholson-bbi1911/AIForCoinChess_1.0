def getMessage(socket_to_server):
    size_of_message_from_server = int(socket_to_server.recv(12).decode())
    message_from_server = socket_to_server.recv(size_of_message_from_server).decode()
    print(message_from_server)
