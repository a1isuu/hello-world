import re
import getpass
from datetime import datetime


def cadastro():
    validacao = False
    # ^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$
    nomeCompleto = str(input('Nome completo: '))
    tag = re.search(
        r"^(?![ ])(?!.*[ ]{2})((?:e|da|do|das|dos|de|d'|D'|la|las|el|los)\s*?|(?:[A-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð'][^\s]*\s*?)(?!.*[ ]$))+$", nomeCompleto)

    if tag:
        print("Validade comprovada. ")
        validacao = True
    else:
        while validacao == False:
            print("O nome %s não é um nome válido! " % nomeCompleto)
            # ^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$
            nomeCompleto = str(input('Insira novamente seu nome completo: '))
            tag = re.search(
                r"^(?![ ])(?!.*[ ]{2})((?:e|da|do|das|dos|de|d'|D'|la|las|el|los)\s*?|(?:[A-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð'][^\s]*\s*?)(?!.*[ ]$))+$", nomeCompleto)
            if tag:
                validacao = True

    validacao = False
    # senha min 8 char, min 1 maiuscula, min 1 num, min 1 simbolo, sem sequencia (ex.: aa, 11)
    senha = str(input('Senha: '))
    tag = re.search(
        r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", senha)

    if tag:
        print("Validade comprovada. ")
        validacao = True
    else:
        while validacao == False:
            print("A senha digitada não é uma senha válida! ")
            # senha min 8 char, min 1 maiuscula, min 1 num, min 1 simbolo, sem sequencia (ex.: aa, 11)
            senha = str(input('Insira sua senha novamente: '))
            tag = re.search(
                r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", senha)
            if tag:
                validacao = True
    # /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}$/

    confirmaSenha = str(input('Confirme sua senha: '))
    while confirmaSenha != senha:
        confirmaSenha = str(
            input('Senhas diferentes. Insira sua confirmação novamente: '))

    validacao = False
    email = str(input('E-mail: '))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)

    if tag:
        print("Validade comprovada. ")
        validacao = True
    else:
        while validacao == False:
            print("O e-mail %s não é e-mail válido! " % email)
            email = str(input('Insira novamente o seu e-mail: '))
            tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
            if tag:
                validacao = True

    confirmaEmail = str(input('Confirmação de E-mail: '))
    while confirmaEmail != email:
        confirmaEmail = str(
            input('E-mails diferentes. Confirme seu e-mail novamente: '))

    dia = str(input('Dia que nasceu: '))
    mes = str(input('Mês que nasceu: '))
    ano = str(input('Ano que nasceu: '))

    print('{0}/{1}/{2}' .format(dia, mes, ano))

    sexo = int
    #escolha = int(input('Selecione 1 - Masculino, 2 - Feminino, 3 - Prefiro não informar ou 4 - Outros'))

    def switch(escolha):
        if escolha == 1:
            return sexo == "Masculino"
        elif escolha == 2:
            return sexo == "Feminino"
        elif escolha == 3:
            return sexo == "Prefiro não informar"
        elif escolha == 4:
            return sexo == "Outros"
    switch(escolha=1)


cadastro()
