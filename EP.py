#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:26:32 2018

@author: manucastilla
"""

#========= fazendo o menu =========
print ("Controle do Estoque:")
print ("0 - sair ")
print ("1 - adicionar item")
print ("2 - remover item")
print ("3 - alterar item")
print ("4 - imprimir estoque")
escolha = int(input("Faça sua escolha: "))

if escolha == 0:
    print ("Até mais")
while 5 > escolha > 0:
    if escolha == 1:
        produto = input("Nome do produto: ")
        quantidade_inicial = int(input("Quantidade inicial: "))
        if quantidade_inicial < 0:
            print ("A quantidade inicial não pode ser negativa.")
            
    