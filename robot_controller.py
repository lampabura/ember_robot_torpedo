
from random import randrange
import socket

ROBOT_HOST = '127.0.0.1'  # The server's hostname or IP address

positive_comments = [
    "Haha",
    "I'm the best",
    "ez peezy lemon squeezy",
    "too ez"
]

negative_comments = [
    "wh",
    "dont cheat",
    "you are such a loser",
    "reported"
]

class RobotController:
    def __init__(self,port):
        super().__init__()
        self.port = port

    def positiveFeedback(self, force=False):
        if randrange(0,100) < 40 or force:
            self.createComment(positive_comments)

    def negativeFeedback(self, force=False):
        if randrange(0, 100) < 40 or force:
            self.createComment(negative_comments)
        
    def createComment(self, possibilities):
        index = randrange(0, len(possibilities))
        response = possibilities[index]
        print("RESPONSE: ", response)
        # Calling robot API
        self.sendMessageToRobot(response)

    def endingComment(self,message):
        self.sendMessageToRobot(message)

    def sendMessageToRobot(self,message):
        if self.port > 0:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ROBOT_HOST, self.port))
                s.settimeout(3)
                s.sendall(str.encode(message))
                data = s.recv(1024)
                s.close()
        
