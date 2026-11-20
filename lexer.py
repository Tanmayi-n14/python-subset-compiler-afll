import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'STRING',
    'EQUALS', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE', 'COLON', 'COMMA',
    'PLUS', 'MINUS', 'STAR', 'DIVIDE', 'MOD', 'POWER',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'WITH', 'AS', 'LAMBDA', 'FROM', 'IMPORT', 'FOR', 'IN', 'IF', 'ELSE'
)

# Multi-character operators
t_POWER    = r'\*\*'
t_GE       = r'>='
t_LE       = r'<='
t_EQ       = r'=='
t_NE       = r'!='

# Single-character tokens
t_EQUALS   = r'='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_COLON    = r':'
t_COMMA    = r','
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_STAR     = r'\*'
t_DIVIDE   = r'/'
t_MOD      = r'%'
t_GT       = r'>'
t_LT       = r'<'

t_ignore   = ' \t'

def t_STRING(t):
    r'(\"[^\"]*\"|\'[^\']*\')'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    keywords = {
        'with': 'WITH', 'as': 'AS', 'lambda': 'LAMBDA',
        'from': 'FROM', 'import': 'IMPORT', 'for': 'FOR',
        'in': 'IN', 'if': 'IF', 'else': 'ELSE'
    }
    t.type = keywords.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
