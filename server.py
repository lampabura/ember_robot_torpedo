#!/usr/bin/env python3

import socket
from game_controller import GameController
from time import sleep

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
TIMEOUT = 10
gameController = GameController()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.settimeout(TIMEOUT)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        startMsg = gameController.startGame()
        print(startMsg)
        conn.sendall(startMsg)

        while not gameController.isEnded():
            data = conn.recv(1024)
            if not data:
                break
            else:
                response = gameController.processMessage(data)
                if response: conn.sendall(response)
                sleep(1)
        print("Disconnected ", addr)
