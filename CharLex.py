import ply.lex as lex

'''
S -> corchete A corcheteF
A -> llave B llaveF
A -> llave B llaveF comma A
B -> key_id dospuntos value_num comma C
C -> key_display dospuntos value_string comma D
D -> key_name dospuntos value_string comma E
E -> key_stack dospuntos value_num 
'''

tokens = (
    'corchete',
    'corcheteF',
    'llave',
    'llaveF',
    'key_id',
    'key_display',
    'key_name',
    'key_stack',
    'dospuntos',
    'value_num',
    'value_string',
    'comma'
)

def t_key_id(t):
    r'"id"'
    return t

def t_key_display(t):
    r'"displayName"'
    return t

def t_key_name(t):
    r'"name"'
    return t

def t_key_stack(t):
    r'"stackSize"'
    return t

def t_value_num(t):
    r'[0-9]+'
    return t

def t_value_string(t):
    r'"[A-Za-z0-9 _\(\)\']+"'
    return t


t_corchete = r'\['
t_corcheteF = r'\]'
t_llave = r'\{'
t_llaveF = r'\}'
t_dospuntos = r':' 
t_comma = r'\,' 

t_ignore  = ' \t\n'

def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == '__main__':

    with open('tacos.json', 'r') as archivo:
        contenido = archivo.read()
    archivo.close()
    print(contenido)
    input_str = ' '
    while input_str != '':
        print('\n ----------Presione ENTER para terminar----------')
        input_str = contenido

        if input_str != '':
            lexer.input(input_str)

            for tok in lexer:
                print(tok)
        break