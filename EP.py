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
escolha = 1
while 5 > escolha and escolha != 0:
    print ("Controle do Estoque:")
    print ("0 - sair ")
    print ("1 - adicionar item")
    print ("2 - remover item")
    print ("3 - alterar item")
    print ("4 - imprimir estoque")
    if escolha == 1:
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
<<<<<<< HEAD
                if alteracao == "a" or alteracao == "A":
                    quantidadeNova = int(input("Inclua quantidade: "))
                    estoque[produto]["quantidade"]+=quantidadeNova
                elif alteracao == "b" or alteracao =="B":
                    preco_novo = float(input("Novo preço unitário: "))
                    if preco_novo > 0:
                        estoque[produto]["preco_unitario"]=preco_novo
=======
                del estoque[produto]
       elif escolha == 3:
            produto = input ("Nome do produto que deseja alterar: ")
            if produto in estoque:
                print ("Tipo de alteração:")
                print ("a - Quantidade ")
                print ("b - Preço unitário")
                alteracao=input("\nEscolha a sua alteração: ")
                if produto not in estoque:
                    print ("Elemento não encontrado")
                elif produto in estoque:
                    if alteracao == "a" or alteracao == "A":
                        quantidadeNova = int(input("Inclua quantidade: "))
                        estoque[produto]["quantidade"]+=quantidadeNova
                    elif alteracao == "b" or alteracao =="B":
                        preco_novo = float(input("Novo preço unitário: "))
                        if preco_novo > 0:
                            estoque[produto]["preco_unitario"]+=preco_novo
                        else:
                            print ("Preço unitário não pode ser negativo.")
>>>>>>> dc8896502d883fb57de7eb4904ee4324bdbafc27
                    else:
                        print ("opção indisponível")
                print ('Novo estoque de {0}: {1}'.format(produto, estoque[produto]))
                print (" ")
            else:
                print("\nProduto não incluso no estoque\n")
       elif escolha == 4:
           print(" ")
           print ("Tipo de estoque:")
           print ("a - Estoque total ")
           print ("b - Apenas os estoques negativos")
           print ("c - Valor monetário em estoque")
           modalidade=input("Escolha a sua modalidade: ")
           if modalidade == "a" or modalidade == "A":
               print(' ')
               for k in estoque:
                   print("Estoque: {0}, quantidade: {1}, preço unitário: {2}".format(k, estoque[k]["quantidade"],estoque[k]["preco_unitario"]))
               print (" ") 
           elif modalidade == "b"or modalidade == "B":
               lista_negativos=[]
               for k in estoque:
                   if estoque[k]["quantidade"] < 0:
                       lista_negativos.append([k,estoque[k]["quantidade"]])
                       print(" ")
                       print ("Os estoques negativos são:")
               if len(lista_negativos)==0:
                    print("\nNão há estoque negativo\n")
               else:
                   for i in range(len(lista_negativos)):
                       print ("Produto: {0}, Quantidade: {1}".format(lista_negativos[i][0], lista_negativos[i][1]))
                   print(" ")
                       
           elif modalidade == "c" or modalidade =="C":
               contador = 0
               for k in estoque:
                   if estoque[k]["quantidade"]>0:
                       contador+=estoque[k]["quantidade"]*estoque[k]["preco_unitario"]
               contador=round(contador,2)
               print ("O valor monetário total em estoque é: {0}".format(contador))
               print(" ")
<<<<<<< HEAD
                   
       elif modalidade == "c" or modalidade =="C":
           contador = 0
           for k in estoque:
               if estoque[k]["quantidade"]>0:
                   contador+=estoque[k]["quantidade"]*estoque[k]["preco_unitario"]
           contador=round(contador,2)
           print ("O valor monetário total em estoque é: {0}".format(contador))
           print(" ")
if escolha == 0:
    print("Até mais")
=======
       else: #incluir opção para quando o usuario dá enter sem ter numero  (evitar erro)
            print("\nNão existe essa opção.\n")
            escolha = 1 #para se manter no while

>>>>>>> dc8896502d883fb57de7eb4904ee4324bdbafc27
original = json.dumps(estoque, sort_keys=True, indent=4)
with open ('estoque_python.txt', 'w') as arquivo:
    arquivo.write(original)
    
    
    
    
        
            
    