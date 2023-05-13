# PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

import ply.yacc as yacc
from CharLex import tokens

Precedence = (
    ('left', 'corchete', 'corcheteF'),
    ('left', 'llave', 'llaveF'),
    ('left', 'key_id', 'key_display', 'key_name', 'key_stack'),
    ('left', 'dospuntos'),
    ('left', 'value_num', 'value_string'),
    ('left', 'comma'),
)


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
    'B : key_id dospuntos value_num comma C'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])


def p_objectDisplay(p):
    'C : key_display dospuntos value_string comma D'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectName(p):
    'D : key_name dospuntos value_string comma E'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_objectStack(p):
    'E : key_stack dospuntos value_num'
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
    break

