# PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

import numpy as np

import ply.yacc as yacc
from CharLex import tokens


#precedence = (
#    ('corchete','corcheteF','llave','llaveF','key','value','comma')
#)

precedence = (
#    ('left', 'dospuntos'),
    ('left', 'llave', 'llaveF', 'corchete', 'corcheteF'),
    ('left', 'key', 'dospuntos','value'),
    ('left', 'comma')

)

'''
S -> A
S -> B
A -> [ B ]
B -> { C }
B -> { C },B
C -> Key : Value
C -> Key : B
C -> Key : Value,C
C -> Key : A
C -> Key : A,C
'''

'''
'corchete',
'corcheteF',
'llave',
'llaveF',
'key',
'value',
'comma',
'dospuntos'
'''

def p_startArray(p):
    'S : A'
    p[0] = p[1]
    print(p[0])

def p_startObject(p):
    'S : B'
    p[0] = p[1]
    print(p[0])

def p_array(p):
    'A : corchete B corcheteF'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_object(p):
    'B : llave C llaveF'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_objectObject(p):
    'B : llave C llaveF comma B'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_data(p):
    #'C : key value'
    #p[0] = p[1] + p[2]
    'C : key dospuntos value'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_dataObject(p):
    #'C : key B'
    #p[0] = p[1] + p[2]
    'C : key dospuntos B'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_dataData(p):
    #'C : key value comma C'
    #p[0] = p[1] + p[2] + p[3] + p[4] 
    'C : key dospuntos value comma C'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_dataArray(p):
    #'C : key A'
    #p[0] = p[1] + p[2]
    'C : key dospuntos A'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_dataArrayData(p):
    #'C : key A comma C'
    #p[0] = p[1] + p[2] + p[3] + p[4] 
    'C : key dospuntos A comma C'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = '{\t"nombre": "Juan",\n\t"edad": 25,\n\t"direccion": {\n\t\t"calle": "Av. Libertador",\n\t\t"numero": 1234\n\t}\n}'
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
