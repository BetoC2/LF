import ply.lex as lex

'''
S -> corchete A corcheteF
A -> llave B llaveF
A -> llave B llaveF comma A
B -> key_id dospuntos value_num comma
B -> key_nombre dospuntos value_string comma
B -> key_precio dospuntos value_num comma
B -> key_descripcion dospuntos value_string 
'''

tokens = (
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
)

t_corchete = r'\['
t_corcheteF = r'\]'
t_llave = r'\{'
t_llaveF = r'\}'
t_key_id = r'"id"'
t_key_nombre = r'"nombre"'
t_key_precio = r'"precio"'
t_key_descripcion = r'"descripcion"'
t_dospuntos = r':' 
t_value_string = r'"[A-Za-z][A-Za-z\.\, 0-9]+"'
t_value_num = r'[0-9]+\.?[0-9]*'
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
    