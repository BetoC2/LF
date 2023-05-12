import ply.lex as lex

tokens = (
    'corchete',
    'corcheteF',
    'llave',
    'llaveF',
    'key',
    'value',
    'comma',
    'dospuntos'
)

t_corchete = r'\['
t_corcheteF = r'\]'
t_llave = r'\{'
t_llaveF = r'\}'
t_key = r'\"[A-Za-z\$_][A-Za-z _\-0-9]+\"'
t_value = r'[0-9]+|(\"[A-z0-9_\.\,\-\{-~]+\")|true|false|([0-9]+\.[0-9]+)'
t_comma = r'\,'
t_dospuntos = r':'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = '\t|\n| '

def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
if __name__ == '__main__':
    input_str = ' '
    while input_str != '':
        print('\n ----------Presione ENTER para terminar----------')
        input_str = input('Entrada a validar: ')

        if input_str != '':
            lexer.input(input_str)

            for tok in lexer:
                print(tok)