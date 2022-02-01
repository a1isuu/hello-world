from itertools import cycle
import re

def cadastroJur():

    resposta = ''
    nomeEmpresa = str(input('Nome da Empresa: '))
    resposta = str(input('Confirma essas informações?\nY - Para sim, N - Para não\n'))
    while (resposta != 'Y') or (resposta != 'y'):    
        if (resposta == 'Y') or (resposta == 'y'):
            break
        if (resposta == 'N') or (resposta == 'n'):
            nomeEmpresa = str(input('Insira novamente o nome da Empresa: '))
            resposta = str(input('Confirma essas informações?\nY - Para sim, N - Para não\n'))
        while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
            if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                break
            if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                resposta = input('Opção inválida, por favor insira Y ou N.\n')
        
    emailEmpresa = str(input('E-mail empresarial: '))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,6}$", emailEmpresa)

    if tag:
        print("Validade comprovada. ")
        validacao = True
    else:
        while validacao == False:
            print("O e-mail %s não é e-mail válido! " % emailEmpresa)
            emailEmpresa = str(input('Insira novamente o e-mail: '))
            tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,6}$", emailEmpresa)
            if tag:
                validacao = True

    confirmaEmail = str(input('Confirmação de E-mail: '))
    while confirmaEmail != emailEmpresa:
        confirmaEmail = str(
            input('E-mails diferentes. Confirme o e-mail novamente: '))

    print('E-mail cadastrado.\n')

    def Localizacao ():
        resposta = ''
        while (resposta != 'Y') or (resposta != 'y'):    
            
            nomeRua = str(input('Insira o nome da rua: '))
            numLocal = int(input('Insira o número: '))
            bairro = str(input('Insira o bairro: '))
            cidade = str(input('Insira a cidade: '))
            estado = str(input('Insira o Estado: '))
            cep = int(input('Insira o código postal: '))
            while (len(str(int(cep))) < 8) or (len(str(int(cep))) > 8):
                cep = int(input('Tamanho inválido. Insira novamente o código postal: '))
                
            print('Rua: {0}\nNúmero: {1}\nBairro: {2}\nCidade: {3}\nEstado: {4}\nCep: {5} ' .format(nomeRua, numLocal, bairro, cidade, estado, cep))

            print('Seu endereço está correto?')
            resposta = input('Y - Sim\nN - Não\n')

            if (resposta == 'Y') or (resposta == 'y'):
                break
            if (resposta == 'N') or (resposta == 'n'):
                while (resposta != 'Y') or (resposta != 'y'):                
                    opcao = int(input('Por favor, informe o número referente ao que deseja mudar.\n1 - Nome da Rua\n2 - Número do Local\n3 - Bairro\n4 - Cidade\n5 - Estado\n6 - CEP\n'))
                    if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6):
                        while (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6):
                            opcao = int(input('Escolha inválida, insira novamente um número de 1 a 6.\n1 - Nome da Rua\n2 - Número do Local\n3 - Bairro\n4 - Cidade\n5 - Estado\n6 - CEP\n'))
                    if opcao == 1:
                        nomeRua = input('Insira o nome da rua: ')
                    if opcao == 2:
                        numLocal = input('Insira o número: ')
                    if opcao == 3:
                        bairro = input('Insira o bairro: ')
                    if opcao == 4:
                        cidade = input('Insira a cidade: ')
                    if opcao == 5:
                        estado = input('Insira o Estado: ')
                    if opcao == 6:
                        cep = input('Insira código postal: ')
                        while (len(str(int(cep))) < 8) or (len(str(int(cep))) > 8):
                            cep = int(input('Tamanho inválido. Insira novamente o código postal: '))
                    
                    print('Rua: {0}\nNúmero: {1}\nBairro: {2}\nCidade: {3}\nEstado: {4}\nCep: {5} ' .format(nomeRua, numLocal, bairro, cidade, estado, cep))

                    print('Seu endereço agora está correto?')
                    resposta = input('Y - Sim\nN - Não\n')
                    if (resposta == 'Y') or (resposta == 'y'):
                        break
                    if (resposta != 'Y') and (resposta != 'y') and (resposta != 'N') and (resposta != 'n'):
                        while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                            print('Resposta invalida, insira novamente')
                            resposta = input('Y - Sim\nN - Não\n')
                            if (resposta == 'Y') or (resposta == 'y'):
                                break
                            if (resposta == 'N') or (resposta == 'n'):
                                break
                            
                if (resposta != 'Y') and (resposta != 'y') and (resposta != 'N') and (resposta != 'n'):
                    while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                        print('Resposta invalida, insira novamente')
                        resposta = input('Y - Sim\nN - Não\n')
                        if (resposta == 'Y') or (resposta == 'y'):
                            break   
            if (resposta == 'Y') or (resposta == 'y'):
                break
    Localizacao()
    cnpj =  int
    tamanho_cnpj = 14

    def is_cnpj_valido(cnpj: str) -> bool:
        if len(cnpj) != tamanho_cnpj:
            return False

        if cnpj in (c * tamanho_cnpj for c in "1234567890"):
            return False

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                return False
        return True

    telContato = str(input('Insira o telefone da empresa: '))
    tipoEmpresa = str(input('Indique como você identifica sua empresa:\n1 - MEI\n2 - EIRELI\n3 - Empresário Individual\n4 - Sociedade Empresária Limitada\n5 - Sociedade Simples\n6 - Sociedade Anônima\n7 - Sociedade Limitada Unipessoal\n'))
    def switch(escolha):
        tipoEmpresa = ''
        if escolha == '1':
            tipoEmpresa = "MEI"
            return tipoEmpresa
        elif escolha == '2':
            tipoEmpresa = "EIRELI"
            return tipoEmpresa
        elif escolha == '3':
            tipoEmpresa = "Empresário Individual"
            return tipoEmpresa
        elif escolha == '4':
            tipoEmpresa = "Sociedade Empresária Limitada"
            return tipoEmpresa
        elif escolha == '5':
            tipoEmpresa = "Sociedade Simples"
            return tipoEmpresa
        elif escolha == '6':
            tipoEmpresa = "Sociedade Anônima"
            return tipoEmpresa
        elif escolha == '7':
            tipoEmpresa = "Sociedade Limitada Unipessoal"
            return tipoEmpresa

    if (tipoEmpresa != '1') or (tipoEmpresa != '2') or (tipoEmpresa != '3') or (tipoEmpresa != '4') or (tipoEmpresa != '5') or (tipoEmpresa != '6') or (tipoEmpresa != '7'):
        while (tipoEmpresa != '1') or (tipoEmpresa != '2') or (tipoEmpresa != '3') or (tipoEmpresa != '4') or (tipoEmpresa != '5') or (tipoEmpresa != '6') or (tipoEmpresa != '7'):
            if (tipoEmpresa == '1') or (tipoEmpresa == '2') or (tipoEmpresa == '3') or (tipoEmpresa == '4') or (tipoEmpresa == '5') or (tipoEmpresa == '6') or (tipoEmpresa == '7'):
                break
            tipoEmpresa = str(input('\nOpção inválida, tente novamente:\n1 - MEI\n2 - EIRELI\n3 - Empresário Individual\n4 - Sociedade Empresária Limitada\n5 - Sociedade Simples\n6 - Sociedade Anônima\n7 - Sociedade Limitada Unipessoal\n'))
    switch(tipoEmpresa)
    tipoEmpresa = switch(tipoEmpresa)
    print('Você identificou sua empresa como: {0}?' .format(tipoEmpresa))
    resposta = str(input('Y - Para sim, N - Para não\n'))
    while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
        if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
            break
        if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
            resposta = input('Opção inválida, por favor insira Y ou N.\n')
    if (resposta == 'Y') or (resposta == 'y'):
        print('Tipo de empresa cadastrado.\n')
    else:
        while (resposta != 'Y') or (resposta != 'y'):
            tipoEmpresa = str(input('Selecione a opção que indique o tipo da sua empresa: '))
            while (tipoEmpresa != '1') or (tipoEmpresa != '2') or (tipoEmpresa != '3') or (tipoEmpresa != '4') or (tipoEmpresa != '5') or (tipoEmpresa != '6') or (tipoEmpresa != '7'):
                if (tipoEmpresa == '1') or (tipoEmpresa == '2') or (tipoEmpresa == '3') or (tipoEmpresa == '4') or (tipoEmpresa == '5') or (tipoEmpresa == '6') or (tipoEmpresa == '7'):
                    break
                if (tipoEmpresa != '1') or (tipoEmpresa != '2') or (tipoEmpresa != '3') or (tipoEmpresa != '4') or (tipoEmpresa != '5') or (tipoEmpresa != '6') or (tipoEmpresa != '7'):
                    tipoEmpresa = str(input('\nOpção inválida, tente novamente:\n1 - MEI\n2 - EIRELI\n3 - Empresário Individual\n4 - Sociedade Empresária Limitada\n5 - Sociedade Simples\n6 - Sociedade Anônima\n7 - Sociedade Limitada Unipessoal\n'))
                
            switch(tipoEmpresa)
            tipoEmpresa = switch(tipoEmpresa)
            print('Você identificou sua empresa como: {0}?' .format(tipoEmpresa))
            resposta = str(input('Y - Para sim, N - Para não\n'))
            while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                if (resposta == 'Y') or (resposta == 'y'):
                    print('Tipo de empresa cadastrado.\n')
                    break
                if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                    break
                if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    resposta = input('Opção inválida, por favor insira Y ou N.\n')
            if (resposta == 'Y') or (resposta == 'y'):
                break
    numFuncionario = int(input('Insira o número de operantes:'))
    porteEmpresa = str(input('Indique o porte da empresa:\n1 - MEI\n2 - ME\n3 - EPP\n'))
    #def switch(escolhe):


    if (porteEmpresa == '1'):
        porteEmpresa == 'MEI'
    if (porteEmpresa == '2'):
        porteEmpresa == 'ME'
    if (porteEmpresa == '3'):
        porteEmpresa == 'EPP'

cadastroJur()



