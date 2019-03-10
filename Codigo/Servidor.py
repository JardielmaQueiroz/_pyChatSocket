#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Servidor.py
#  
# Trabalho de Redes 2017/2 - Jardielma Queiroz de Lima

import socket

#--------------------------------------- Configuração do Servidor ------------------------------------------
host = '0.0.0.0'  # Endereço que o servidor vai receber definido como 0.0.0.0 pq pode receber qualquer ip 
porta = 3333  # Porta que o Servidor escuta
Servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria mecanismo de Socket para receber a conexão
endereco = (host, porta) #Define o endereço do servidr
Servidor.bind(endereco) #define para qual IP e porta o servidor deve aguardar a conexão
Servidor.listen(10) #Define o limite de ip que o servidor escuta
#-----------------------------------------------------------------------------------------------------------
  

def lerArquivo():
	lista = []
	arq = open("usuarios.txt", "rt")
	linha = arq.readline()
	
	while linha != "":
		linha = linha.strip('\n')
		lista.append(linha)
		linha = arq.readline()
	#fim 
	arq.close()
	return lista
#fim função

def validaLogin(pacote,listUser):
	nome = pacote['usuario']
	for i in range(len(listUser)):
		if(nome == listUser[i]):
			return True
		#fim
	return False
#fim funcao

def validaRemetenteMsg(msg,listUser):
	nome = msg[1]
	for i in range(len(listUser)):
		if(nome == listUser[i]):
			return True
		#fim
	return False
#fim funcao

def trataLogin(log,pacote):
	if log:
		resp = trataPacote(pacote['usuario'],'sucesso')
		enviaPacote(resp)
	else:
		resp = trataPacote(pacote['usuario'],'falha')
		enviaPacote(resp)
	
	return resp 
#fim funcao 
	
def trataPacote(usuario,operacao):
    pacote = {}
    pacote['usuario'] = usuario
    pacote['operacao'] = operacao
    return pacote
#fim funcao

def enviaPacote(send):
    send = str(send)
    msg = bytes(send, 'utf-8')
    con.send(msg)
#fim funcao

def recebePacote():
	resp = con.recv(1024)
	if resp != '':
		resposta = eval(resp.decode('utf-8'))
		return resposta
	else:
		resposta = trataPacote('servidor','sair')
	return resposta
#fim função

def recebeMenssagem():
	resp = con.recv(1024)
	resp = resp.decode('utf-8')
	return resp
#fim funcao

def buscaMsg(nomeRemet,matMsg):
	listMsg = []
	for linha in range (len(matMsg)):
		if(nomeRemet == matMsg[linha][1]):
			#print(matMsg[linha])
			listMsg.append(matMsg[linha])
		#fim
	#fim for
	return listMsg
#fim funcao 

def apagaMsg(lst, mat):
	m = 0
	for l  in range(len(lst)):
		while m < (len(mat)):
			if lst[l] == mat[m]:
				del mat[m]
				m = (len(mat))
			#fim if
			m = m+1
		#fim while
	#fim for
	return mat
#fim função

def sair():
    con.close()
    print("Conexão Encerrada")
    print('\n Aguardando alguem se conectar..')
#fim funcao

def main():

	#declaração de Váriaveis:
	global con
	listaUsuario = []
	matMsg = []
	
	listaUsuario = lerArquivo()
	#print(listUser)
	
	
	print('---------- Servidor Unicializado - Aguardando alguém se conectar! -------------\n')
    #aceita um conexão
	print('Aguardando...')
	while True:
		#aceita uma conexão:
		con,cliente = Servidor.accept()
		print('\n Detalhes da Conexão: \n\n',con)	
		print('Conectado: ',cliente)
		
		#Tratando o Login Usuário
		pacote = recebePacote()
		log = validaLogin(pacote,listaUsuario)
		pacote = trataLogin(log,pacote)
		print(pacote)
		if pacote['operacao'] == 'falha':
			while pacote['operacao'] != 'sucesso':
				if pacote['operacao'] == 'falha':
					pacote = recebePacote()
				#fim if
				log = validaLogin(pacote,listaUsuario)
				pacote = trataLogin(log,pacote)
				print(pacote)
			#fim while
		#fim if
		
		#Tratamento de Menssagens
		pacote = recebePacote()
		while pacote['operacao'] != 'sair':
			if pacote['operacao'] == 'enviar':
				print(pacote)
				enviaPacote("Informa o destinatario: ")
				msg = recebePacote()
				d = msg[1]
				if (validaRemetenteMsg(msg,listaUsuario)):
					enviaPacote("\n Menssagem Enviada com Sucesso!!")
					matMsg.append(msg)
					print(matMsg)
				else:
					enviaPacote("\n Falha ao enviar Menssagem, remetente não cadastrado!!") 
			if pacote['operacao'] == 'ler':
				print(pacote)
				enviaPacote("ok")
				nomeRemet = recebeMenssagem()
				listaMsg = buscaMsg(nomeRemet,matMsg)
				enviaPacote(listaMsg)
				if (len(matMsg) > 0):
					matMsg = apagaMsg(listaMsg, matMsg)
				#fim if
			if pacote['operacao'] == 'sair':
				print(pacote)
				enviaPacote("ok")
			
			pacote = recebePacote()
		#fim while
		
		#fechando uma conexão
		sair()
		#Processamento	

	#return 0

if __name__ == '__main__':
	main()

