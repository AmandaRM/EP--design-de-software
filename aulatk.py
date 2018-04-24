#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:20:56 2018

@author: manucastilla
"""

import tkinter as tk

def diz_oi():
    print ("boa")

window = tk.Tk()

botao = tk.Button(window)
botao.configure(text="aperta aqui!")
botao.configure(command=diz_oi)
botao.grid()

window.mainloop()