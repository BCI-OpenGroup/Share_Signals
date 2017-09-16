#Cliente

import socket

def menu():
	print("-----------Opciones-------------")
	print("                                ")
	print("1-Listar datos EEG              ")
	print("2-Descargar todos los datos EEG ")
	print("3-Salir                         ")
	print("--------------------------------")
	print("                                ")

def opcion(option,cliente):
	if(option=='1'):
		print "SEND LIST"
		cliente.send("list_files_eeg")
		respuesta=cliente.recv(4096)
	if(option=='2'):
		pass


servidor="127.0.0.1"
puerto=5000

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((servidor,puerto))
cliente.send("ok servidor")
respuesta=cliente.recv(4096)

print respuesta

salir=False
while ~salir:
	menu()
	option=raw_input(">>")
	if(option=='3'):
		salir=True
	else:
		opcion(option,cliente)