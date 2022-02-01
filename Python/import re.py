import re

class SingUp:
    def __init__(self):
        self.nomeCompleto = None
        self.senha = None
        self.confirmaSenha = None
        self.email = None
        self.confirmaEmail = None
        self.dataNas = None
        self.sexo = None
    def cadastro():

        nomeCompleto = str(input('Nome completo'))#/[A-Z][a-z]* [A-Z][a-z]*/
        tag = re.search(r"/[A-Z][a-z]* [A-Z][a-z]*/", nomeCompleto)
    
        if tag in nomeCompleto:
            print("Validade comprovada. ")
            
        else:
            print("O nome %s não é um nome válido! " %nomeCompleto)