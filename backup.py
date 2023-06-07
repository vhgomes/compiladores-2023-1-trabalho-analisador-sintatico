def expressao(self):
        self.termo()
        while self.current_token is not None and self.current_token[0] == 'Operadores' and self.current_token[1] in ('+', '-'):
            if self.current_token[1] == '+':
                self.avancar()
                self.termo()
            elif self.current_token[1] == '-':
                self.avancar()
                self.termo()

    def termo(self):
        self.factor()
        while self.current_token is not None and self.current_token[0] == 'Operadores' and self.current_token[1] in ('*', '/'):
            if self.current_token[1] == '*':
                self.avancar()
                self.factor()
            elif self.current_token[1] == '/':
                self.avancar()
                self.factor()

    def factor(self):
        if self.current_token[0] == 'Delimitador' and self.current_token[1] == '(':
            self.avancar()
            self.expressao()
            if self.current_token[0] != 'Delimitador' or self.current_token[1] != ')':
                raise SyntaxError("Invalid syntax")
            self.avancar()
        else:
            int(self.current_token[1])
            self.avancar()
    
