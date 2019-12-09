def getMessage(socket_to_server):
    message_from_server = socket_to_server.recv(12).decode()
    while message_from_server == "\r\n":
        message_from_server = socket_to_server.recv(12).decode()
    size_of_message_from_server = int(message_from_server)
    message_from_server = socket_to_server.recv(size_of_message_from_server).decode()
    print("Server> " + message_from_server)


def sendMessage(socket_to_server, message):
    message_length = int(len(message))
    socket_to_server.send(message_length.to_bytes(2, 'big'))
    socket_to_server.send(message.encode())
    socket_to_server.send((0).to_bytes(0, 'big'))
