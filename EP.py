#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
import json
with open ('estoque_python.txt', 'r') as arquivo:
    estoque=arquivo.read()
    estoque=json.loads(estoque)
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
       #incluir print pra quando o item já for exixtente
       produto = input("Nome do produto: ")
       quantidade_inicial = int(input("Quantidade inicial: "))
       estoque[produto]=quantidade_inicial
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
            quantidade = int(input("Quantidade: "))
            estoque[produto]+=quantidade
            print ('Novo estoque de {0}: {1}'.format(produto, estoque[produto]))
   elif escolha == 4:
       print (estoque) # ver se da para imprimir do jeito como fala no pdf
if escolha == 0:
    estoquestr=json.dumps(estoque, sortkeys=True, ident = 4 )
    print ("Até mais")
with open ('estoque_python.txt', 'w') as arquivo:
    arquivo.write(estoquestr)
    
    
    
    
        
            
    