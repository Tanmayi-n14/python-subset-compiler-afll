import ply.yacc as yacc
from lexer import tokens

# Operator precedence (BODMAS + comparisons + power)
precedence = (
    ('left', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'DIVIDE', 'MOD'),
    ('right', 'POWER'),
    ('right', 'UMINUS', 'UPLUS')
)

def p_statement(p):
    '''
    statement : list_comprehension_stmt
              | with_stmt
              | lambda_assignment
              | from_import_stmt
              | set_declaration
              | expression
    '''
    p[0] = p[1] if p[1] is not None else True
    print("Parsed a valid statement.")

# -------------------------
# LIST COMPREHENSIONS
# -------------------------
def p_list_comprehension_basic(p):
    'list_comprehension_stmt : ID EQUALS LBRACKET expression FOR ID IN ID RBRACKET'
    p[0] = ('list_comp', p[1], p[4], p[6], p[8])
    print(f"Found list comprehension for variable '{p[1]}'")

def p_list_comprehension_if(p):
    'list_comprehension_stmt : ID EQUALS LBRACKET expression FOR ID IN ID IF expression RBRACKET'
    p[0] = ('list_comp_if', p[1], p[4], p[6], p[8], p[10])
    print(f"Found list comprehension with condition for '{p[1]}'")

# -------------------------
# WITH STATEMENT
# -------------------------
def p_with_stmt(p):
    'with_stmt : WITH function_call AS ID COLON'
    p[0] = ('with', p[2], p[4])
    print(f"Found 'with' statement for variable '{p[4]}'")

# -------------------------
# LAMBDA EXPRESSION
# -------------------------
def p_lambda_assignment(p):
    'lambda_assignment : ID EQUALS LAMBDA arg_list COLON expression'
    p[0] = ('lambda', p[1], p[4], p[6])
    print(f"Found lambda function assignment for '{p[1]}'")

# -------------------------
# IMPORTS
# -------------------------
def p_from_import_stmt(p):
    'from_import_stmt : FROM ID IMPORT import_list'
    p[0] = ('from_import', p[2], p[4])
    print(f"Found import statement from '{p[2]}' -> {p[4]}")

def p_import_list(p):
    '''
    import_list : import_item
                | import_list COMMA import_item
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_import_item(p):
    '''
    import_item : ID
                | ID AS ID
                | STAR
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '*':
        p[0] = '*'
    else:
        p[0] = (p[1], 'as', p[3])

# -------------------------
# SET DECLARATION
# -------------------------
def p_set_declaration(p):
    'set_declaration : ID EQUALS LBRACE item_list_opt RBRACE'
    p[0] = ('set', p[1], p[4])
    print(f"Found set declaration for '{p[1]}'")

def p_arg_list(p):
    '''
    arg_list : ID
             | arg_list COMMA ID
             | empty
    '''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = p[1] + [p[3]]

def p_item_list_opt(p):
    '''
    item_list_opt : item_list
                  | empty
    '''
    p[0] = p[1] if p[1] is not None else []

def p_item_list(p):
    '''
    item_list : expression
              | item_list COMMA expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# -------------------------
# EXPRESSIONS (BODMAS + comparisons + ternary + unary)
# -------------------------
def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression STAR expression
               | expression DIVIDE expression
               | expression MOD expression
               | expression POWER expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression EQ expression
               | expression NE expression
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_ternary(p):
    'expression : expression IF expression ELSE expression'
    p[0] = ('ternary', p[1], p[3], p[5])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_group(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]

def p_term_unary(p):
    '''
    term : MINUS term %prec UMINUS
         | PLUS term %prec UPLUS
    '''
    p[0] = ('unary', p[1], p[2])

def p_term_value(p):
    '''
    term : ID
         | NUMBER
         | STRING
    '''
    p[0] = p[1]

def p_function_call(p):
    '''
    function_call : ID LPAREN arg_string_list RPAREN
    '''
    p[0] = ('func_call', p[1], p[3])

def p_arg_string_list(p):
    '''
    arg_string_list : STRING
                    | arg_string_list COMMA STRING
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ('{p.value}') on line {p.lineno}")
    else:
        print("Syntax error at end of input.")

parser = yacc.yacc()
