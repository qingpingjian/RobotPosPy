# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:37:03 2018

@author: Administrator
"""

import socket
import SocketServer
import RPi.GPIO as GPIO
import time
import string
import threading

GPIO.setwarnings(False)
IN1 = 18
IN2 = 23
IN3 = 24
IN4 = 25
IOMODE = GPIO.BCM

def GPIOinit():
    print("init function")
    GPIO.setmode(IOMODE)        #设置树莓派的编码格式
    GPIO.setup(IN1, GPIO.OUT)   #设置树莓派GPIO接口为输出，IN1-IN4为4个直流电机对应的接口
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def GPIOreset():
    print("reset function")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def GPIOclean():
    print("clean function")
    GPIO.cleanup()


# 前进
def forward():
    print("move forward")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# 后退
def back():
    print("move backward")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# 左转弯, IN1 & IN2 -> 左面后退，IN3 & IN4 -> 而右面前进
def left():
    print("move left")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# 右转弯， IN1 & IN2 -> 左面前进，IN3 & IN4 -> 而右面后退
def right():
    print("move right")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# 停车
def stop():
    print("stop car")
    GPIOreset()

COMMANDS = ("Forward", "Backward", "Left", "Right", "Stop")

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        clientAddr = self.client_address[0]
        print("Accepted connection from: %s" % (clientAddr))
        GPIOreset()
        print("Car Prepared and Wait for Commands")
        isRunning = False
        while True:
            data = self.request.recv(256).strip()
            if data != "":
                self.request.send(data)
                print("Receive command: %s and Reply back for log." % (data))
                # Starts with '\0' and len(data), I don't know why now
                # print("Data %s and length: %d" % (data, len(data)))
                data = data[2:]
                if not isRunning:
                    # 希望能在开始运动的时候，轮子能尽快开始转动
                    GPIOreset()
                    isRunning = True
                if data == COMMANDS[0]:
                    forward()
                elif data == COMMANDS[1]:
                    back()
                elif data == COMMANDS[2]:
                    left()
                elif data == COMMANDS[3]:
                    right()
                elif data == COMMANDS[4]:
                    stop()
                    if isRunning:
                        isRunning = False
                else:
                    print("Unkown Command:%s" % (data))
            else:
                break
            time.sleep(0.1)
        return

if __name__ == "__main__":
    # TCP server configuration
    HOST = "0.0.0.0"
    PORT = 50010
    # LISTEN = 5
    tcpServer = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server until interrupt the process with Ctrl-C
    try:
        print("Car Prepareing")
        GPIOinit()
        GPIOreset()
        print("Server starts Now")
        tcpServer.serve_forever()
    except KeyboardInterrupt:
        print("Ctrl-C Stopped the server")
    finally:
        print("Clean GPIO")
        GPIOclean()
        print("Shutdown the Server")
        tcpServer.shutdown()
    print("Done.")
        
