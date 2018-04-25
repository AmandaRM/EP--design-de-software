
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
import json
#with open ('geral.txt', 'r') as arquivo:
#    estoque=json.loads(arquivo.read())
geral={}
print('Controle de estoques de lojas:')
print("0 - sair")
print("1 - acessar estoque de loja")
print("2 - adicionar loja")
print("3 - Excluir loja")
opcao=int(input("Selecione sua opção: "))
while 3 > opcao >0:
    if opcao == 2:
        loja=input("Nome da loja: ")
        if opcao in arquivo:
            print('Loja já exxitente')
        loja[estoque]=3
    elif opcao == 1:
        loja=input('Digite o nome da loja que quer acessar: ')
        if loja not in arquivo:
            print('Loja não exixtente')
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
                   if quantidade_inicial < 0:
                       print ("A quantidade inicial não pode ser negativa.")
                       quantidade_inicial = int(input("Quantidade inicial: "))
                   [loja][estoque][produto]={}
                   [loja][estoque][produto]["quantidade"]=quantidade_inicial
                   preco_unitario=float(input("Preço unitário: "))
                   if preco_unitario<0:
                       print ("O preço unitário não pode ser negativo.")
                       preco_unitario=float(input("Preço unitário: "))
                   [loja][estoque][produto]["preco_unitario"]=preco_unitario
           elif escolha ==2:
                produto = input ("Nome do produto a ser removido: ")
                if produto not in estoque:
                    print ("Elemento não encontrado")
                elif produto in estoque:
                    del [loja][estoque][produto]
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
                            [loja][estoque][produto]["quantidade"]+=quantidadeNova
                        elif alteracao == "b" or alteracao =="B":
                            preco_novo = float(input("Novo preço unitário: "))
                            if preco_novo > 0:
                                [loja][estoque][produto]["preco_unitario"]=preco_novo
                            else:
                                print ("Preço unitário não pode ser negativo.")
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
                           lista_negativos.append([k,[loja][estoque][k]["quantidade"]])
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
                       if [loja][estoque][k]["quantidade"]>0:
                           contador+=[loja][estoque][k]["quantidade"]*[loja][estoque][k]["preco_unitario"]
                   contador=round(contador,2)
                   print ("O valor monetário total em estoque é: {0}".format(contador))
                   print(" ")
        
        if escolha == 0:
            print("Até mais")
        elif opcao== 2:
            loja=input('loja a ser removida: ')
            if loja not in arquivo:
                print('Loja inexistente')
            del loja
original = json.dumps(estoque, sort_keys=True, indent=4)
with open ('geral.txt', 'w') as arquivo:
    arquivo.write(original)
    
    
    
    
        
            
    