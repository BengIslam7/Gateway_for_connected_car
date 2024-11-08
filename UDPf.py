import socket
import os
import time
os.system("sudo ifconfig eth0 up")
time.sleep(5)
UDP_IP = "10.10.0.111"  # Replace with the target IP address
UDP_PORT = 7       # Replace with the target port

message = "f"  # send the message via socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print("**Closing**")
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    print("UDP Packet sent to STM32F7")
    print(message.encode())
    print("*************")
finally:
    sock.close()
    os.system("sudo ifconfig eth0 down")
    time.sleep(5)


