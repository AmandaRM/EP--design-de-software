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
   if escolha == 1:
       produto = input("Nome do produto: ")
       if produto in estoque:
           print ("item já existente.")
           print (" ")
       else:
           quantidade_inicial = int(input("Quantidade inicial: "))
           estoque[produto]={}
           estoque[produto]["quantidade"]=quantidade_inicial
           if quantidade_inicial < 0:
               print ("A quantidade inicial não pode ser negativa.")
               quantidade_inicial = int(input("Quantidade inicial: "))
   elif escolha ==2:
        produto = input ("Nome do produto a ser removido: ")
        if produto not in estoque:
            print ("Elemento não encontrado")
        elif produto in estoque:
            del estoque[produto]
   elif escolha == 3:
        produto = input ("Nome do produto que deseja alterar: ")
        if produto not in estoque:
            print ("Elemento não encontrado")
        elif produto in estoque:
            quantidadeNova = int(input("Quantidade: "))
            estoque[produto]["quantidade"]+=quantidadeNova
            print ('Novo estoque de {0}: {1}'.format(produto, estoque[produto]))
   elif escolha == 4:
       print(' ')
       for k in estoque:
           print ('produto: {0}, quantidade: {1}'.format(k,estoque[k]["quantidade"]))
       print(' ') 
if escolha == 0:
    print ("Até mais")
original = json.dumps(estoque, sort_keys=True, indent=4)
with open ('estoque_python.txt', 'w') as arquivo:
    arquivo.write(original)
    
    
    
    
        
            
    