# Import the necessary modules
# Part 1
import re
import ply.lex as lex
import ply.yacc as yacc

#Part 2
# Define the tokens for the lexer
tokens = [
    'NUMBER', # Integer or decimal number
    'PLUS',   # Addition operator
    'MINUS',  # Subtraction operator
    'TIMES',   # Multiplication operator
    'DIVIDE',  # Division operator
    'LPAREN',  # Left parenthesis
    'RPAREN',   # Right parenthesis
]

# Define the regular expressions for each token
t_PLUS    = r'\+'  # Plus sign
t_MINUS   = r'-'   # Minus sign
t_TIMES   = r'\*'   # Asterisk
t_DIVIDE  = r'/'    # Forward slash
t_LPAREN  = r'\('   # Left parenthesis
t_RPAREN  = r'\)'   # Right parenthesis
t_NUMBER  = r'\d+'   # Match one or more digits

# Part 3
# Define how to handle whitespace
t_ignore = ' \t'    # Ignore spaces and tabs

# Define what to do when a syntax error is encountered
def t_error(t):
    print(f"Invalid character '{t.value[0]}'")
    t.lexer.skip(1)  # Skip the erroneous character

# Create the lexer
lexer = lex.lex()

# Part 4
# Define the grammar rules for the parser
def p_expression_plus(p):
    'expression : expression PLUS term'    # Match expression + term
    p[0] = p[1] + p[3]                  # Compute the result
    print(f"{p[1]} + {p[3]} = {p[0]}")  # Print the result

#Part 5
def p_expression_minus(p):
    'expression : expression MINUS term'     # Match expression - term
    p[0] = p[1] - p[3]                      # Compute the result
    print(f"{p[1]} - {p[3]} = {p[0]}")      # Print the result

#Part 6
def p_expression_term(p):
    'expression : term'      # Match a term by itself
    p[0] = p[1]             # Set the result to the term

# Part 7
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
    print(f"{p[1]} * {p[3]} = {p[0]}")

# Part 8
def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
    print(f"{p[1]} / {p[3]} = {p[0]}")

# Part 9
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# Part 10
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = int(p[1])
    print(f"Number: {p[0]}")

# Part 11
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Part 12
# Define what to do when a syntax error is encountered
def p_error(p):
    print("Syntax error in input!")

# Part 13
# Create the parser using YACC
parser = yacc.yacc()

# Part 14
# Prompt the user to input an expression to evaluate
while True:
    try:
        s = input('enter number: ')
    except EOFError:
        break

    # Parse and evaluate the expression
    print("Parsing:")
    result = parser.parse(s)
    print(f"Result: {result}\n")