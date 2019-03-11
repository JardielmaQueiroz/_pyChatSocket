# _pyChatSocket_
<P align="justify">&nbsp&nbsp Chat simples utilizando a biblioteca de programação Socket na linguagem Python, com um lado do cliente e um lado do servidor. Atividade desenvolvida na disciplina de Redes no semestre 2017/1.</p>

### 1. OBJETIVO<br>
<P align="justify">&nbsp&nbsp O objetivo do trabalho é desenvolver uma aplicação cliente/servidor, utilizando a biblioteca de programação Socket na linguagen Python.</p>

### 1. ESPECIFICAÇÂO<br>
<P align="justify">&nbsp&nbsp Ao iniciar o servidor ele irá ler um arquivo com os logins dos usuários cadastrados no sistema, sendo
1 login por linha. Após carregar os usuários na memória o servidor aguardará por conexões na porta TCP 3333.</p>

**<P align="justify"> Quanto um cliente é iniciado, ele peguntará ao usuário qual o seu login. Após ler o login, o cliente irá:</p>**

-  conectar-se ao servidor;
-  baixar as mensagens do usuário, se houver;
-  apresentar na tela; 
-  desconectar-se;  
-  solicitar ao usuário se ele deseja enviar uma mensagem;

**<P align="justify"> Caso o usuário deseje enviar uma mensagem, deverá seguir os seguintes passos:</p>**

-  inserir o login do destinatário;
-  inserir a mensagem;
-  enviar a mensagem para o servidor;

**<P align="justify"> Por outro lado, o servidor ao receber uma mensagem irá:</p>**

-   checar se existe o login do destinatário;
-   caso exista, armazena a mensagem relativa aquele destinatário na memória;
-   caso não existe descarte a mensagem;

<P align="justify"> <b>Nota 1:</b> A aplicação cliente conecta-se ao servidor, realiza uma ação (baixar mensagens, enviar
mensagens) e desconecta-se do servidor. Com isso várias aplicações clientes podem se conectar ao servidor,
sendo uma de cada vez.</p>

<P align="justify"> <b>Nota 2:</b> Após uma mensagem ser lida por um cliente, o servidor apagará a mensagem da memória.
Desta forma, o servidor deverá manter apenas as mensagens não lidas de cada usuário.</p>
