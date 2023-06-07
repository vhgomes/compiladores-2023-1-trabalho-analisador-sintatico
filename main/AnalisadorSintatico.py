from LexicoEnum import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.avancar()

    def verificar_token(self, classe, valor_esperado):
        print(f'Qual index estamos recebendo? Index == {self.index} valoratual = {self.tokens[index]}  Token Atual =={classe}  Valor Esperado == {valor_esperado}')
        tokenzinho = self.tokens[self.index]
        print(f'{tokenzinho[0], tokenzinho[1]}')
        if tokenzinho[0] == classe and (tokenzinho[1] == valor_esperado or valor_esperado is None):
            print('Passou na verificação, foi para o proximo token')
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
                        self.declaracaoBlock()


    def declaracaoParam(self):
        print("Entrou na declaram de PARAM")
        while self.verificar_token(Token.DELIMITADOR, None):
            if self.verificar_token(Token.IDENTIFICADOR, None):
                pass
        return
    
    def declaracaoBlock(self):
        if self.verificar_token(Token.DELIMITADOR, '{'):
            while not self.verificar_token(Token.DELIMITADOR, '}') and self.current_token == None:
                self.declaracao()

                    
    def declaracaoVar(self):
        if self.verificar_token(Token.IDENTIFICADOR, None):
            if self.verificar_token(Token.OPERADORES, '='):
                self.expression()
        pass

    def expression(self):
        self.assigment()


    def assigment(self):
        if self.verificar_token(Token.IDENTIFICADOR, None):
            pass
        self.logica_or()

    def logica_or(self):
        self.logica_and()
        if self.verificar_token(Token.OPERADORES, "or"):

    def logica_and(self):
        self.equalidade()

    def equalidade(self):

    def keyword(self):
        pass
