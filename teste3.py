# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:51:34 2018

@author: Amanda
"""

import json
estoque =  {'chuchu':2, 'abacaxi':3}
estoquestr= json.dumps(estoque)

estoque = json.loads(estoquestr)
print(estoquestr[5])
print(estoque)
print(estoque['chuchu'])
