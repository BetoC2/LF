# PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

import ply.yacc as yacc
from CharLex import tokens


'''
S -> corchete A corcheteF
A -> llave B llaveF
A -> llave B llaveF comma A
B -> key_id dospuntos value_num comma B
B -> key_nombre dospuntos value_string comma B
B -> key_precio dospuntos value_num comma B
B -> key_descripcion dospuntos value_string 
'''

'''
'corchete',
'corcheteF',
'llave',
'llaveF',
'key_id',
'key_nombre',
'key_precio',
'key_descripcion',
'dospuntos',
'value_num',
'value_string',
'comma'
'''

def p_start(p):
    'S : corchete A corcheteF'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_arrayObject(p):
    'A : llave B llaveF'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_arrayObjectObject(p):
    'A : llave B llaveF comma A'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectId(p):
    'B : key_id dospuntos value_num comma B'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectNombre(p):
    'B : key_nombre dospuntos value_string comma B'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectPrecio(p):
    'B : key_precio dospuntos value_num comma B'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectDescripcion(p):
    'B : key_descripcion dospuntos value_string'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
with open('tacos.json', 'r') as archivo:
        contenido = archivo.read()
archivo.close()

while True:
    try:
        s = contenido
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

