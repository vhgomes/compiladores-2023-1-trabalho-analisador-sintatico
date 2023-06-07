from LexicoEnum import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.avancar()

    def verificar_token(self, classe, valor_esperado):
        print(f'Qual index estamos? {self.index}{self.current_token}{valor_esperado}')
        tokenzinho = self.tokens[self.index]
        print(f'{tokenzinho[0], tokenzinho[1]}')
        if tokenzinho[0] == classe and (valor_esperado is None or tokenzinho[1] == valor_esperado):
            print('Entrou na verificação')
            self.avancar()
            return True
        print('Retornando falso?')
        return False
        

    def avancar(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None
        self.declaracao()
        if self.current_token is not None:
            raise SyntaxError("Invalid syntax")
    
    def declaracao(self):
        print(f'Entrou em declaração com o Token {self.current_token}')
        if self.verificar_token(Token.DECLARATION, "fun"):
            self.declaracaoFuncao()
            return
        if self.current_token[1] == 'var':
            self.declaracaoVar()
        else:
            self.keyword()

    def declaracaoFuncao(self):
        if self.verificar_token(Token.IDENTIFICADOR, None):
            if self.verificar_token(Token.DELIMITADOR, '('):
                if self.verificar_token(Token.IDENTIFICADOR, None):
                    self.declaracaoParam()
                    if self.verificar_token(Token.DELIMITADOR, ')'):
                        print('Teoricamente é pra estar aqui')


    def declaracaoParam(self):
        if self.verificar_token(Token.IDENTIFICADOR, None):
            if self.verificar_token(Token.DELIMITADOR, ','):
                print('Delimitador')
                if self.verificar_token(Token.IDENTIFICADOR):
                    pass
                    
    def declaracaoVar(self):
        pass

    def keyword(self):
        pass
