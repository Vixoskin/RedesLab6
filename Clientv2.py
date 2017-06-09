import socket

c =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('172.16.32.104',50001))

print("Ingrese nombre de usuario:")
i =raw_input()
c.send(i)

while True:
	i =raw_input()
	c.send(i)

c.close()