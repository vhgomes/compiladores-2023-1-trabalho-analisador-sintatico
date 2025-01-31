from AnalisadorLexico import tokenizar_codigo_fonte
from AnalisadorSintatico import Parser
import re

with open('test/teste2.c', 'r') as file:
    input = file.read()
    input = re.sub('//.*', ' ', input)  
    input = re.sub('(/\*(.|\n)*?\*/)', ' ', input)  
    tokens = tokenizar_codigo_fonte(input)
    parser = Parser(tokens)
    parser.parse()