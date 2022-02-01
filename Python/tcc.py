import re

def cadastro():
    nomeCompleto = str(input('Nome completo'))#^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$
    tag = re.search(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", nomeCompleto)
   
    if tag:
        print("Validade comprovada. ")
    else:
        print("O nome %s não é um nome válido! " %nomeCompleto)


    senha = str(input('Senha'))#senha min 8 char, min 1 maiuscula, min 1 num, min 1 simbolo, sem sequencia (ex.: aa, 11)
    tag = re.search(r"/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}$/", senha)
    
    if tag:
        print("Validade comprovada. ")
    else:
        print("A senha digitada não é uma senha válida! " %senha)
    confirmaSenha = str(input('Confirmação de senha'))#/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}$/

    
    email = str(input('E-mail'))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
    
    if tag:
        print("Validade comprovada. ")
    else:
        print("O e-mail %s não é e-mail válido! " %email)

    confirmaEmail = str(input('Confirmação de E-mail'))
    
    if confirmaEmail != email:
        print('E-mail não possui semelhança. Escreva-o novamente')
    else:
        return

    
    dataNas = str(input('Data de nascimento'))
    sexo = int
    #escolha = int(input('Selecione 1 - Masculino, 2 - Feminino, 3 - Prefiro não informar ou 4 - Outros'))

    def switch(escolha):
        if escolha == 1:
            return sexo == "Masculino"
        elif escolha==2:
            return sexo == "Feminino"
        elif escolha==3:
            return sexo == "Prefiro não informar"
        elif escolha==4:
            return sexo == "Outros"
    switch(escolha=1)
cadastro()