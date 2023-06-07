from enum import Enum
import re

class Token(Enum):
    ESPACO_BRANCO = re.compile(r'\s+')
    DECLARATION = re.compile(r'\b(fun|var)')
    IDENTIFICADOR = re.compile(r'[a-zA-Z_]\w*')
    KEYWORD = re.compile(r'\b(int|char|long|short|float|double|void|if|else|for|while|do|break|continue|struct|switch|case|default|return|printf)\b')
    OPERADORES = re.compile(r'(\+\+|--|\+=|-=|\*=|/=|%=|==|!=|<=|>=|&&|\|\||[;+\-*/%.,<>&|!^=~])')
    OPERADORES_LOGICOS = re.compile(r'\b(or|and)')
    INTEIROS = re.compile(r'\d+')
    TEXTUAL = re.compile(r'\".*?\"')
    PONTO_FLUTUANTE = re.compile(r'(\d+\.\d+)')
    DELIMITADOR = re.compile(r"\[|\]|\(|\)|\{|\}|\;|\,|\:")