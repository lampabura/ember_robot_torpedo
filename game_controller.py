
import json
from types import SimpleNamespace
from game import Game
from helpers import Message,Command,State
from robot_controller import RobotController

class GameController:
    
    def __init__(self):
        self.game = Game()
        self.robot = RobotController()

    def startGame(self):
        msg = Message()
        msg.command = Command.START
        return self.encodeMessage(msg)
    
    def endGame(self):
        msg = Message()
        msg.command = Command.YOUWIN
        return self.encodeMessage(msg)

    def decodeMessage(self,data):
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    def encodeMessage(self, msg):
        return str.encode(json.dumps(msg.__dict__))

    def processMessage(self,raw_data):
       
        msg = self.decodeMessage(raw_data)
        
        print(msg.command, " - ",self.game.state)

        if self.game.state == State.START and msg.command == Command.START:
            self.game.start()
            return raw_data # send back start message

        if self.game.state == State.INGAME and msg.command == Command.START:
            msg.command = Command.STEP
            msg.row, msg.column = self.game.getStep()
            return self.encodeMessage(msg)

        if self.game.state == State.INGAME and msg.command == Command.STEP:
            
            # Create robot feedback if enemy got hit our ship
            isNegative = self.game.stepEnemy(msg.row, msg.column)

            if self.game.isEnded():
                print("I LOST")
                self.game.ended()
                self.robot.negativeFeedback(True)
                return self.endGame()

            if isNegative: 
                self.robot.negativeFeedback()
            else: 
                self.robot.positiveFeedback()
           
            msg.row, msg.column = self.game.getStep()
            return self.encodeMessage(msg)

        if self.game.state == State.INGAME and msg.command == Command.YOUWIN:
            print("I WIN")
            self.robot.positiveFeedback(True)
            self.game.ended()

    def isEnded(self):
        return self.game.isEnded()

