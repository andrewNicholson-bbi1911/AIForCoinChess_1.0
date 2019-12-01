import socket


class AiPlayer:
    port = 5000
    ip = 'localhost'

    def connect(self):
        socket_to_server = socket.socket()
        socket_to_server.connect((self.ip, self.port))
        while True:
            size_of_message_from_server = int(socket_to_server.recv(12).decode())
            message_from_server = socket_to_server.recv(size_of_message_from_server).decode()
            print(message_from_server)
            break
        sending_message = "Connected"
        sending_message_length = int(len(sending_message));
        sending_message_length2 = int(len(sending_message))+1;
        socket_to_server.send(sending_message_length.to_bytes(1, 'big'))
        socket_to_server.send(sending_message.encode())
        socket_to_server.send((0).to_bytes(0, 'big'))



newAIPlayer = AiPlayer()
newAIPlayer.connect()
