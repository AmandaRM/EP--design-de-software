
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
import json
from firebase import firebase
'''
firebase = firebase.FirebaseApplication('https://ep-estoque-em-nuvem.firebaseio.com/', None)
if firebase.get("dados", None) is None:
    estoque = {}
else:
    estoque = firebase.get("dados", None)
 '''   
with open ('geral.txt', 'r') as arquivo:
    estoque=json.loads(arquivo.read())

opcao=1

while 4 > opcao >0:
########### imprimindo as opções para LOJA##########
    print('Controle de estoques de lojas:')
    print("0 - sair")
    print("1 - acessar estoque de loja")
    print("2 - adicionar loja")
    print("3 - Excluir loja")
    opcao=int(input("Selecione sua opção: "))
    
########### ADICIONAR LOJA ##########    
    if opcao == 2:
        loja=input("Nome da loja: ")
        if loja in estoque:
            print('Loja já existente! Tente novamente')
        else:
            estoque[loja]={}
            print ("\nloja adicionada\n")

########### ACESSAR ESTOQUE DE UMA LOJA ##########    
    elif opcao == 1:
        loja=input('Digite o nome da loja que quer acessar: ')
        if loja not in estoque:
            print('\nLoja não existente\n')
            loja=input('Digite o nome da loja que quer acessar: ')
        escolha=1
        
########### PARA ACESSAR NOS ESTOQUES ##########  
        while 5 > escolha >= 0:
           print ("Controle do Estoque:")
           print ("0 - sair ")
           print ("1 - adicionar item")
           print ("2 - remover item")
           print ("3 - alterar item")
           print ("4 - imprimir estoque")
           escolha = int(input("Faça sua escolha: "))
           
           ###### ADICIONAR ITEM ######
           if escolha == 1:
               produto = input("Nome do produto: ")
               if produto in loja:
                   print ("item já existente.")
                   print (" ")
               else:
                   quantidade_inicial = int(input("Quantidade inicial: "))
                   if quantidade_inicial < 0:
                       print ("A quantidade inicial não pode ser negativa.")
                       quantidade_inicial = int(input("Quantidade inicial: "))
                   estoque[loja][produto]={}
                   estoque[loja][produto]["quantidade"]=quantidade_inicial
                   preco_unitario=float(input("Preço unitário: "))
                   if preco_unitario<0:
                       print ("O preço unitário não pode ser negativo.")
                       preco_unitario=float(input("Preço unitário: "))
                   estoque[loja][produto]["preco_unitario"]=preco_unitario
                   
           ###### REMOVER ITEM ######
           elif escolha ==2:
                produto = input ("Nome do produto a ser removido: ")
                if produto not in estoque[loja]:
                    print ("Elemento não encontrado")
                elif produto in estoque[loja]:
                    del estoque[loja][produto]
           
           ###### ALTERAR ITEM ######
           elif escolha == 3:
                produto = input ("Nome do produto que deseja alterar: ")
                if produto in estoque[loja]:
                    print ("Tipo de alteração:")
                    print ("a - Quantidade ")
                    print ("b - Preço unitário")
                    alteracao=input("\nEscolha a sua alteração: ")
                    if produto not in estoque[loja]:
                        print ("Elemento não encontrado")
                    elif produto in estoque[loja]:
                        if alteracao == "a" or alteracao == "A":
                            quantidadeNova = int(input("Inclua quantidade: "))
                            estoque[loja][produto]["quantidade"]=quantidadeNova
                        elif alteracao == "b" or alteracao =="B":
                            preco_novo = float(input("Novo preço unitário: "))
                            if preco_novo > 0:
                                estoque[loja][produto]["preco_unitario"]=preco_novo
                            else:
                                print ("Preço unitário não pode ser negativo.")
                        else:
                            print ("opção indisponível")
                    print ('Novo estoque de {0}: {1}'.format(produto, estoque[loja][produto]))
                    print (" ")
                else:
                    print("\nProduto não incluso no estoque\n")
                    
           ###### IMPRIMIR ESTOQUE ######
           elif escolha == 4:
               ###### TIPOS DE ESTOQUE ######
               print(" ")
               print ("Tipo de estoque:")
               print ("a - Estoque total ")
               print ("b - Apenas os estoques negativos")
               print ("c - Valor monetário em estoque")
               modalidade=input("Escolha a sua modalidade: ")
               
               ###### ESTOQUE TOTAL ######
               if modalidade == "a" or modalidade == "A":
                   print(' ')
                   for k in estoque[loja]:
                       print("Produto: {0}, quantidade: {1}, preço unitário: {2}".format(k, estoque[loja][k]["quantidade"],estoque[loja][k]["preco_unitario"]))
                   print (" ") 
                   if estoque[loja]== {}:
                       print ("\nestoque vazio\n")
                       
               ###### IMPRIMIR OS NEGATIVOS ######
               elif modalidade == "b"or modalidade == "B":
                   lista_negativos=[]
                   for k in estoque[loja]:
                       if estoque[loja][k]["quantidade"] < 0:
                           lista_negativos.append([k,estoque[loja][k]["quantidade"]])
                           print(" ")
                           print ("Os estoques negativos são:")
                   if len(lista_negativos)==0:
                        print("\nNão há estoque negativo\n")
                   else:
                       for i in range(len(lista_negativos)):
                           print ("Produto: {0}, Quantidade: {1}".format(lista_negativos[i][0], lista_negativos[i][1]))
                       print(" ")
               
               ###### VALOR MONETÁRIO ######
               elif modalidade == "c" or modalidade =="C":
                   contador = 0
                   for k in estoque[loja]:
                       if estoque[loja][k]["quantidade"]>0:
                           contador+=estoque[loja][k]["quantidade"]*estoque[loja][k]["preco_unitario"]
                   contador=round(contador,2)
                   print ("O valor monetário total em estoque é: {0}".format(contador))
                   print(" ")
                   
           ###### SAIR DO ESROQUE ######
           elif escolha == 0:
                    print("\nAté mais\n")
                    break
                
    ###### LOJA SER REMOVIDA ######
    elif opcao == 3:
        loja=input('loja a ser removida: ')
        if loja not in estoque:
            print('Loja inexistente')
        else:
            del estoque[loja]
            print('Loja excluída!')
     
###### SAIR DE TUDO ######    
if opcao ==0:
   print("Até mais!")

original = json.dumps(estoque, sort_keys=True, indent=4)
with open ('geral.txt', 'w') as arquivo:
     arquivo.write(original)
    
#firebase.patch('https://ep-estoque-em-nuvem.firebaseio.com', estoque)    
    
    
        
            
    