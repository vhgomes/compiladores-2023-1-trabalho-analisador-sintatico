from LexicoEnum import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.avancar()

    def verificar_token(self, classe, valor_esperado = None):
        print(f'Qual index estamos? {self.index}{self.current_token}')
        tokenzinho = self.tokens[self.index]
        print(f'{tokenzinho[0], tokenzinho[1]}')
        if tokenzinho[0] == classe and tokenzinho[1] == valor_esperado:
            print('Entrou na verificação')
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
        if self.current_token[1] == 'var':
            self.declaracaoVar()
        else:
            self.keyword()

    def declaracaoFuncao(self):
        self.avancar()
        if self.verificar_token(Token.IDENTIFICADOR):
            print("Passou por ser um identificador")
            if self.verificar_token(Token.DELIMITADOR, '('):
                print('Entrou em delimitador de abertura')
                self.avancar()
                print("Passou por ser a abertura de um delimitador de função")
                if self.verificar_token(Token.DELIMITADOR, ')'):
                    print('fechou a função')
                    pass
                    
    def declaracaoVar(self):
        pass

    def keyword(self):
        pass
