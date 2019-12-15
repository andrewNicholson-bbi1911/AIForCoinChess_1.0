import socket
from IScripts.ActionsWithServer import getMessage, sendMessage


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
        sendMessage(socket_to_server, sending_message)
        while True:
            getMessage(socket_to_server)
            sendMessage(socket_to_server, input("AI (you)> "))


newAIPlayer = AiPlayer()
newAIPlayer.Connect()
