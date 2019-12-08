import socket
from IScripts.ActionsWithServer import getMessage


class AiPlayer:
    port = 5000
    ip = 'localhost'

    def connect(self):
        socket_to_server = socket.socket()
        socket_to_server.connect((self.ip, self.port))
        while True:
            getMessage(socket_to_server)
            break
        sending_message = "Connected"
        sending_message_length = int(len(sending_message))
        socket_to_server.send(sending_message_length.to_bytes(2, 'big'))
        socket_to_server.send(sending_message.encode())
        socket_to_server.send((0).to_bytes(0, 'big'))


newAIPlayer = AiPlayer()
newAIPlayer.connect()
