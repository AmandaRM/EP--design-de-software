#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
import json
with open ('estoque_python.txt', 'r') as arquivo:
    estoque=json.loads(arquivo.read())
escolha=1
while 5 > escolha > 0:
   print ("Controle do Estoque:")
   print ("0 - sair ")
   print ("1 - adicionar item")
   print ("2 - remover item")
   print ("3 - alterar item")
   print ("4 - imprimir estoque")
   escolha = int(input("Faça sua escolha: "))
   if escolha<0:
       print("Não existe essa opção.")
       escolha = int(input("Faça sua escolha: "))   
   elif escolha == 1:
       produto = input("Nome do produto: ")
       if produto in estoque:
           print ("item já existente.")
           print (" ")
       else:
           quantidade_inicial = int(input("Quantidade inicial: "))
           if quantidade_inicial < 0:
               print ("A quantidade inicial não pode ser negativa.")
               quantidade_inicial = int(input("Quantidade inicial: "))
           estoque[produto]={}
           estoque[produto]["quantidade"]=quantidade_inicial
           preco_unitario=float(input("Preço unitário: "))
           if preco_unitario<0:
               print ("O preço unitário não pode ser negativo.")
               preco_unitario=float(input("Preço unitário: "))
           estoque[produto]["preco_unitario"]=preco_unitario
   elif escolha ==2:
        produto = input ("Nome do produto a ser removido: ")
        if produto not in estoque:
            print ("Elemento não encontrado")
        elif produto in estoque:
            del estoque[produto]
   elif escolha == 3:
        produto = input ("Nome do produto que deseja alterar: ")
        print ("Tipo de alteração:")
        print ("a - Quantidade ")
        print ("b - Preço unitário")
        alteracao=input("Escolha a sua alteração: ")
        if produto not in estoque:
            print ("Elemento não encontrado")
        elif produto in estoque:
            if alteracao == "a" or alteracao == "A":
                quantidadeNova = int(input("Nova quantidade: "))
                estoque[produto]["quantidade"]+=quantidadeNova
            elif alteracao == "b" or alteracao =="B":
                preco_novo = float(input("Novo preço unitário: "))
                if preco_novo > 0:
                    estoque[produto]["preco_unitario"]+=preco_novo
                else:
                    print ("Preço unitário não pode ser negativo.")
            else:
                print ("opção indisponível")
        print ('Novo estoque de {0}: {1}'.format(produto, estoque[produto]))
        print (" ")
   elif escolha == 4:
       print(' ')
       for k in estoque:
           print("Estoque: {0}, quantidade: {1}, preço unitário: {2}".format(k, estoque[k]["quantidade"],estoque[k]["preco_unitario"]))
       print (" ") 
if escolha == 0:
    print("Até mais")
original = json.dumps(estoque, sort_keys=True, indent=4)
with open ('estoque_python.txt', 'w') as arquivo:
    arquivo.write(original)
    
    
    
    
        
            
    