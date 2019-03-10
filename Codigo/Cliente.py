#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cliente.py
#  
# Trabalho de Redes 2017/2 - Jardielma Queiroz de Lima

import socket

#-----------------------------Configuração de Socket---------------------------------
host = '127.0.0.1'  # Endereco IP do Servidor
porta = 3333  # Porta que o Servidor esta
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket TCP/Padrão IPV 4
endereco = (host, porta) #Define o endereço do servidr
#------------------------------------------------------------------------------------

def enviaPacote(send):
	send = str(send)
	msg = bytes(send, 'utf-8')
	cliente.send(msg)
#fim funcao

def recebePacote():
	resp = cliente.recv(1024)
	if resp != '':
		resposta = eval(resp.decode('utf-8')) #eval converte de str para dict
		return resposta
	else:
		resposta = trataPacote('servidor','sair')
	return resposta
#fim função

def trataPacote(nomeUser,operacao):
    pacote = {}
    pacote['usuario'] = nomeUser
    pacote['operacao'] = operacao
 
    return pacote
#fim funcao

def efetuarlogin():
	usuario = str(input('Informe seu Login:'))
	pacote = trataPacote(usuario,'entrar')
	enviaPacote(pacote)
	resp = recebePacote()

	return resp
#fim funcao

def criaMsg(remet, dest, msg):
	menssage = []
	menssage.append(remet)
	menssage.append(dest)
	menssage.append(msg)	
	return menssage
#fim funcao

def recebeMenssagem():
	resp = cliente.recv(1024)
	resp = resp.decode('utf-8')
	return resp
#fim funcao

def imprimeMsg(listaMsg):
	print("-----------------------------")
	for i in range(len(listaMsg)): 
		print('Remetente:',listaMsg[i][0])
		print('Menssagem:',listaMsg[i][2])
		print("-----------------------------")
	#fim for
#fim funcao

def main():

	#conectando ao Servidor:
	cliente.connect(endereco)
	
	#Validando usuário:
	log = efetuarlogin()
	while log['operacao'] != 'sucesso':
		print('\n--------- Usuário não existe!! Verifique Seu Login e tente novamente. ---------\n')
		log = efetuarlogin()
	#fim while
	
	if log['operacao'] == 'sucesso':
		print('\n >>>',log['usuario'], 'conectado!!')
	#fim if
	
	#Operações:
	print('\n ************************************** MENU ***********************************')
	print('	1: Enviar Menssagem	2: Ler Menssagem	3: Sair')
	print('\n ************************************** **** ***********************************')
	
	try:
		op = int(input('>> '))
		while ((op > 0) and (op < 4)):
			if op == 1:
				log['operacao'] = 'enviar'
				enviaPacote(log)
				mem = recebeMenssagem()
				dest = str(input(mem))
				m = str(input("Digite sua msg: \n "))
				msg = criaMsg(log['usuario'], dest, m)
				enviaPacote(msg)
				confirma = recebeMenssagem()
				print(confirma)
			#fim if enviar
			if op == 2:
				log['operacao'] = 'ler'
				enviaPacote(log)
				ler = recebeMenssagem()
				enviaPacote(log['usuario'])
				listaMsg = eval(recebeMenssagem())
				print(log['usuario'],' você possui', len(listaMsg), 'mensagem(s)!\n\n')
				if(len(listaMsg) > 0):
					imprimeMsg(listaMsg)
				#fim if			
			#fim if ler
			if op == 3:
				log['operacao'] = 'sair'
				enviaPacote(log)
				print('\n >>>',log['usuario'], " desconectou-se")
				cliente.close()
			#fim if sair
			if op == ""	:
				log['operacao'] = 'sair'
				enviaPacote(log)
				print('\n >>>',log['usuario'], " desconectou-se")
				cliente.close()
			#fim if vazio
			op = int(input('>> '))
		#fim while
	except:
		log['operacao'] = 'sair'
		enviaPacote(log)
		print('\n >>>',log['usuario'], " desconectou-se")
		cliente.close()
	#fim excecao
	
	return 0

if __name__ == '__main__':
	main()

