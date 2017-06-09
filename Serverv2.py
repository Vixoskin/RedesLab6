import socket
import threading

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.16.32.104",50001))
s.listen(2)

def Msn(sock,adrr):
	User = sock.recv(1024)

	while True:
		print (User)
		datos = sock.recv(1024)
		print (datos)

while True:
	sock, addr =s.accept()
	t=threading.Thread(target = Msn,args=(sock,addr))
	t.start()

sock.close()

s.close()