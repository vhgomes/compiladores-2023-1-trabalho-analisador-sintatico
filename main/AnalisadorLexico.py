import re
from LexicoEnum import Token


def tokenizar_codigo_fonte(codigo_fonte):
    tokens = []
    
    posicao = 0
    while posicao < len(codigo_fonte):
        # Nesse trecho de código, ele verifica se é um espaço em branco, caso seja, ele só pula para a próxima parte do código
        match_espaco_branco = Token.ESPACO_BRANCO.value.match(codigo_fonte, posicao)
        if match_espaco_branco:
            posicao = match_espaco_branco.end()
            continue

        match_declaration = Token.DECLARATION.value.match(codigo_fonte, posicao)
        if match_declaration:
            tokens.append((Token.DECLARATION, match_declaration.group()))
            posicao = match_declaration.end()
            continue

        match_identificador = Token.IDENTIFICADOR.value.match(codigo_fonte, posicao)
        if match_identificador:
            identificador = match_identificador.group()
            match_keyword = Token.KEYWORD.value.match(codigo_fonte, posicao)
            if match_keyword:
                tokens.append((Token.KEYWORD, match_keyword.group()))
                posicao = match_keyword.end()
            match_operador_logico = Token.OPERADORES_LOGICOS.value.match(codigo_fonte, posicao)
            if match_operador_logico:
                tokens.append((Token.OPERADORES_LOGICOS.match_keyword.group()))
                posicao = match_operador_logico.end()
            else:
                tokens.append((Token.IDENTIFICADOR, identificador))
                posicao += len(identificador)
            continue

        match_textual = Token.TEXTUAL.value.match(codigo_fonte, posicao)
        if match_textual:
            tokens.append((Token.TEXTUAL, match_textual.group()))
            posicao += len(match_textual.group())
            continue

        match_delimitador = Token.DELIMITADOR.value.match(codigo_fonte, posicao)
        if match_delimitador:
            tokens.append((Token.DELIMITADOR, match_delimitador.group()))
            posicao += len(match_delimitador.group())
            continue
        
        match_operadores = Token.OPERADORES.value.match(codigo_fonte, posicao)
        if match_operadores:
            tokens.append((Token.OPERADORES, match_operadores.group()))
            posicao += len(match_operadores.group())
            continue

        match_ponto_flutuante = Token.PONTO_FLUTUANTE.value.match(codigo_fonte, posicao)
        if match_ponto_flutuante:
            tokens.append((Token.PONTO_FLUTUANTE, match_ponto_flutuante.group()))
            posicao += len(match_ponto_flutuante.group())
            continue

        match_inteiros = Token.INTEIROS.value.match(codigo_fonte, posicao)
        if match_inteiros:
            tokens.append((Token.INTEIROS, match_inteiros.group()))
            posicao += len(match_inteiros.group())
            continue

        raise RuntimeError(f'Token não identificado na posição => {posicao} {codigo_fonte[posicao]}')
    
    return tokens

if __name__ == '__main__':
    with open('testes/teste3.c', 'r') as file:
        input = file.read()
        input = re.sub('//.*', ' ', input)  
        input = re.sub('(/\*(.|\n)*?\*/)', ' ', input)  
        tokens = tokenizar_codigo_fonte(input)
        for token in tokens:
            print(token)
