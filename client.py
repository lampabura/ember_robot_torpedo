#!/usr/bin/env python3

import socket
from time import sleep
from game_controller import GameController

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
TIMEOUT = 10
STEP_SLEEP_TIME = 3
ROBOT_PORT = 65319

gameController = GameController(ROBOT_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(TIMEOUT)
    while not gameController.isEnded():
        data = s.recv(1024)
        if not data: break
        response = gameController.processMessage(data)
        if response: s.send(response)
        sleep(STEP_SLEEP_TIME)
s.close()

