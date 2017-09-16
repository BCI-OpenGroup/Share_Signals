#Server program

import socket
import threading
import os


def conexiones(socket_cliente):
	peticion=socket_cliente.recv(1024)
	if(peticion=="ok servidor"):
		print "[*] Mensaje recibido: %s" % peticion
		socket_cliente.send("ok")
	if(peticion=="list_files_eeg"):
		print("list files")
		Send_File_List(socket_cliente)

def Send_File_List(socket_cliente):
	print "[*] Peticione Lista Ficheros ..."
	path_files="./DATA_EEG"
	lista=ls(path_files) #Listamos todos los ficheros del directorio indicado
	for i in range(1,length(lista)):
		socket_cliente.send(lista(i))

def Send_All_Files(path_files,name_file,soscket_cliente):
	pass

ip="0.0.0.0"
puerto=5000
max_conexiones=150
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind((ip,puerto))
servidor.listen(max_conexiones)

print "[*] Escuchando conexiones en %s: %d" % (ip,puerto)

while True:
	cliente,direccion=servidor.accept()
	print "[*] Conexion establecida con %s: %d" % (direccion[0],direccion[1])
	conexiones=threading.Thread(target=conexiones,args=(cliente,))
	conexiones.start()