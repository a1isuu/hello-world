import re
import os
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

    print('Nome cadastrado.\n')

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

    print('Senha cadastrada.\n')

    validacao = False
    email = str(input('E-mail: '))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,6}$", email)

    if tag:
        print("Validade comprovada. ")
        validacao = True
    else:
        while validacao == False:
            print("O e-mail %s não é e-mail válido! " % email)
            email = str(input('Insira novamente o seu e-mail: '))
            tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,6}$", email)
            if tag:
                validacao = True

    confirmaEmail = str(input('Confirmação de E-mail: '))
    while confirmaEmail != email:
        confirmaEmail = str(
            input('E-mails diferentes. Confirme seu e-mail novamente: '))

    print('E-mail cadastrado.\n')

    resposta = ''
    while (resposta != 'Y') or (resposta != 'y'):
        dia = int(input('Dia que nasceu: '))
        if (dia <= 0) or (dia > 31):
            while (dia == 0) or (dia > 31):
                dia = int(input('Dia invalido, insira-o novamente: '))
        mes = int(input('Mês que nasceu: '))
        if (mes <= 0) or (mes > 12):
            while (mes <= 0) or (mes > 12):
                mes = int(input('Mês invalido, insira-o novamente: '))
        ano = int(input('Ano que nasceu: '))
        anoAtual = 2021
        idade = anoAtual - ano
        if idade < 18:
            print('Não é possível prosseguir com o cadastro. Idade informada é menor que 18 anos.')
            exit()
        elif idade > 99:
            print('Não é possível prosseguir com o cadastro. Idade informada é aposentada.')
            exit()   
        else:
            print('{0}/{1}/{2}' .format(dia, mes, ano))
            print('Confirma essas informações?\nY - Para sim, N - Para não')
            resposta = str(input(''))
            if (resposta == 'Y') or (resposta == 'y'):
                break        
            while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                    break
                if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    resposta = input('Opção inválida, por favor insira Y ou N.\n')

    print('Data {0}/0{1}/{2} confirmada.\n' .format(dia, mes, ano))
    
    # escolha = int(input('Selecione 1 - Masculino, 2 - Feminino, 3 - Prefiro não informar ou 4 - Outros'))

    sexo = str(input('Selecione a opção que indique seu gênero:\n1 - Masculino\n2 - Feminino\n3 - Prefiro não informar\n4 - Outros\n'))

    def switch(escolha):
        sexo = ''
        if escolha == '1':
            sexo = "Masculino"
            return sexo
        elif escolha == '2':
            sexo = "Feminino"
            return sexo
        elif escolha == '3':
            sexo = "Prefiro não informar"
            return sexo
        elif escolha == '4':
            sexo = "Outros"
            return sexo

    if (sexo != '1') or (sexo != '2') or (sexo != '3') or (sexo != '4'):
        while (sexo != '1') or (sexo != '2') or (sexo != '3') or (sexo != '4'):
            if (sexo == '1') or (sexo == '2') or (sexo == '3') or (sexo == '4'):
                break
            sexo = str(input('\nOpção inválida, tente novamente:\n1 - Masculino\n2 - Feminino\n3 - Prefiro não informar\n4 - Outros\n'))

    switch(sexo)
    sexo = switch(sexo)
    print('Você se identificou como: {0}?' .format(sexo))
    resposta = str(input('Y - Para sim, N - Para não\n'))
    while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
        if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
            break
        if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
            resposta = input('Opção inválida, por favor insira Y ou N.\n')
    if (resposta == 'Y') or (resposta == 'y'):
        print('Gênero cadastrado.\n')
    else:
        while (resposta != 'Y') or (resposta != 'y'):
            sexo = str(input('Selecione a opção que indique seu gênero: '))
            while (sexo != '1') or (sexo != '2') or (sexo != '3') or (sexo != '4'):
                if (sexo == '1') or (sexo == '2') or (sexo == '3') or (sexo == '4'):
                    break
                if (sexo != '1') or (sexo != '2') or (sexo != '3') or (sexo != '4'):
                    sexo = str(input('\nOpção inválida, tente novamente:\n1 - Masculino\n2 - Feminino\n3 - Prefiro não informar\n4 - Outros\n'))
                
            switch(sexo)
            sexo = switch(sexo)
            print('Você se identificou como: {0}?' .format(sexo))
            resposta = str(input('Y - Para sim, N - Para não\n'))
            while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                if (resposta == 'Y') or (resposta == 'y'):
                    print('Gênero cadastrado.\n')
                    break
                if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                    break
                if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    resposta = input('Opção inválida, por favor insira Y ou N.\n')
            if (resposta == 'Y') or (resposta == 'y'):
                break

    resposta = ''
    while (resposta != 'Y') or (resposta != 'y'):
        cpf = input('Insira seu CPF (sem as pontuações):\n')
        if (len(cpf) <= 10) or (len(cpf) > 11):
            while len(cpf) != 11:
                print('Tamanho inválido.')
                cpf = input('Insira-o novamente (sem as pontuações):\n')
        resposta = input(cpf[:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'-'+cpf[9:]+' esta correto? Y - Para sim, N - Para não.\n')
        if (resposta == 'Y') or (resposta == 'y'):
            break
        if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
            while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                resposta = input('Opção inválida, por favor insira Y ou N.\n')
                if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                    break
        if (resposta == 'Y') or (resposta == 'y'):
            break
    print('CPF cadastrado.\n')


    resposta = ''
    while (resposta != 'Y') or (resposta != 'y'):

        telefone = input('Insira seu número de telefone (0DDD e número):\n')
        ddd = str(telefone[:3])
        numero = str(telefone[3:])
            
        if (len(numero) < 9) or (len(numero) > 9):
            if (len(numero) < 9):
                print('Seu número de telefone possui números a menos.')
            if (len(numero) > 9):
                print('Seu número de telefone possui números a mais.')
            while (len(numero) < 9) or (len(numero) > 9):
                print('Seu número de telefone é inválido.')
                telefone = input('Digite-o novamnente (DDD e número):\n')
                ddd = str(telefone[:3])
                numero = str(telefone[3:])
        print(f'({ddd}){numero[:5]}-{numero[5:]}')
        resposta = input('Esse é seu número de telefone? Y - Para sim, N - Para não.\n')
        if (resposta == 'Y') or (resposta == 'y'):
            break
        if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    resposta = input('Opção inválida, por favor insira Y ou N.\n')
                    if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                        break
        if (resposta == 'Y') or (resposta == 'y'):
            break
    print(f'({ddd}){numero[:5]}-{numero[5:]} cadastrado com sucesso.\n')

    perguntaEmpr = input('Você possui uma empresa?\n1 - Sim\n2 - Não\n')    
    while (perguntaEmpr != '1') or (perguntaEmpr != '2'):
        if perguntaEmpr == '1':
            break
        if perguntaEmpr == '2':
            break
        if (perguntaEmpr != '1') or (perguntaEmpr != '2'):
            print('Resposta inválida. Responda novamente.')
            perguntaEmpr = input('Você possui uma empresa?\n1 - Sim\n2 - Não\n')

    pergTermos = input('Você aceita os termos e condições?\n1 - Sim\n2 - Não\n')
    while (pergTermos != '1') or (pergTermos != '2'):
        if pergTermos == '1':
            break
        if pergTermos == '2':
            break
        if (pergTermos != '1') or (pergTermos != '2'):
            print('Resposta inválida. Responda novamente.')
            pergTermos = input('Você aceita os termos e condições?\n1 - Sim\n2 - Não\n')
cadastro()
#os.system('cls')