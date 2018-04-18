#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
import json
with open ('estoque_python.json', 'r') as arquivo:
    estoque=arquivo.read()    
if len(estoque)==0:
    estoque={}
else:
    estoque=json.loads(estoque)
    print ("Controle do Estoque:")
    print ("0 - sair ")
    print ("1 - adicionar item")
    print ("2 - remover item")
    print ("3 - alterar item")
    print ("4 - imprimir estoque")
    escolha = int(input("Faça sua escolha: "))
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
                # ver o que tem de errado nessa linha de cima
        elif escolha == 4:
            #copia_estoque = estoque.split(',')
            print (estoque.split(','))
    if escolha == 0:
        estoquestr=json.dump(estoque)
        print ("Até mais")
with open ('estoque_python.json', 'w') as arquivo:
    arquivo.write(estoquestr)
    
    
    
    
        
            
    