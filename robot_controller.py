
from random import randrange


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
    def positiveFeedback(self, force=False):
        if randrange(0,100) < 40 or force:
            self.createComment(positive_comments)

    def negativeFeedback(self, force=False):
        if randrange(0, 100) < 40 or force:
            self.createComment(negative_comments)
        
    def createComment(self, possibilities):
        index = randrange(0, len(possibilities))
        print("RESPONSE: ", possibilities[index])
        ##TODO call robot api
