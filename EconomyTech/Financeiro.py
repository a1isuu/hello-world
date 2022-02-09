import os

def financeiro():
    
    def switch(escolha):
        opcaoFinan = ''
        if escolha == 1:
            opcaoFinan = "Gastos"
        
            mediaDespesas = float(input('Insira a média de despesas no último mês: '))
            print('{0}$ foram gastos no último mês.' .format(mediaDespesas))
            vendasMes = float(input('Agora insira o valor ganho no último mês: '))
            print('R${0} representam o valor ganho no último mês.' .format(vendasMes))
            gastos = mediaDespesas / vendasMes
            print(f'Os gastos tiveram uma porcentagem de {gastos}%\n')
            return gastos
        elif escolha == 2:
            opcaoFinan = "Lucro"
            receitasTotais = float(input('Insira o faturamento obtido com as vendas: '))
            print('R${0} de faturamento.' .format(receitasTotais))
            custos = float(input('Agora insira os custos para a execução do trabalho: '))
            print('R${0} foram gastos para a conclusão do produto.' .format(custos))
            lucro = receitasTotais - custos
            margemLucro = lucro / receitasTotais
            print('Foi obtida uma margem de lucro de {0}%\ncom um lucro bruto final de R${1}\n' .format(margemLucro, lucro))
            return margemLucro
        elif escolha == 3:
            opcaoFinan = "Faturamento"
            precoVenda = float(input('Insira o preço de venda da unidade produzida: '))
            print('{0}$ é o valor de cada unidade vendida.' .format(precoVenda))
            quantVendas = float(input('Agora insira a quantidade de unidades vendidas: '))
            print(quantVendas, 'unidades foram vendidas')
            faturamento = precoVenda * quantVendas
            print('R${0} foram faturados com as vendas.\n' .format(faturamento))
            resposta = str(input('Gostaria de saber o faturamento líquido obtido nessas vendas? *(Selecione caso tenham ocorrido devoluções do produto ou se paga impostos)\nY - Para sim, N - Para não\n'))
            while (resposta != 'N') or (resposta != 'n'):
                if (resposta == 'N') or (resposta == 'n'):
                    break
                if (resposta == 'Y') or (resposta == 'y'):
                    deducVendas = float(input('Insira quantos itens da mesma unidade foram devolvidos: '))
                    print(deducVendas, 'itens dessa unidade foram devolvidos e/ou cancelados.')
                    impostos = float(input('Agora insira a porcentagem de impostos paga: '))
                    print('{0}%'' de impostos aplicados ao calculo.' .format(impostos))
                    fatuLiq = (faturamento - deducVendas) - (impostos / 100)
                    print('R${0} de faturamento líquido foram obtidos com as vendas' .format(fatuLiq))
                    break
                while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                        break
                    if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                        resposta = input('Opção inválida, por favor insira Y ou N.\n')
            return faturamento, fatuLiq
            
    def folhaPag():
    
        salBruto = float(input('Insira o valor do salário bruto do funcionário: '))
        dependentes = int(input('Insira o número de dependentes do funcionário: '))
        if (dependentes > 0):
            salBruto -= (dependentes * 189.59)
        outros = float(input('Outros descontos além do INSS e do IRRF: '))
        
        if (salBruto <= 1212):
            INSS = 1212 * 0.075
        elif (salBruto >= 1212.01 and salBruto <= 2427.35):
            INSS1 = 1212 * 0.075
            INSS2 = (salBruto - 1212) * 0.09
            INSS = INSS1 + INSS2
        elif (salBruto >= 2427.36 and salBruto <= 3641.03):
            INSS1 = 1212 * 0.075
            INSS2 = 1215.35 * 0.09 
            INSS3 = (salBruto - 2427.35) * 0.12
            INSS = INSS1 + INSS2 + INSS3
        elif (salBruto >= 3641.04 and salBruto <= 7087.22):
            INSS1 = 1212 * 0.075
            INSS2 = 1215.35 * 0.09 
            INSS3 = 1213.68 * 0.12
            INSS4 = (salBruto - 3641.03) * 0.14
            INSS = INSS1 + INSS2 + INSS3 + INSS4
        elif (salBruto > 7087.22):
            INSS1 = 1212 * 0.075
            INSS2 = 1215.35 * 0.09 
            INSS3 = 1213.68 * 0.12
            INSS4 = 3446.19 * 0.14
            INSS5 = 992.21
            INSS = INSS1 + INSS2 + INSS3 + INSS4 + INSS5
        
        if (salBruto <= 1903.98):
            IRRF = salBruto * 0.0
        elif (salBruto >= 1903.99 and salBruto <= 2826.65):
            IRRF = (salBruto * 0.075) - 142.80
        elif (salBruto >= 2826.66 and salBruto <= 3751.05):
            IRRF = (salBruto * 0.15) - 354.80
        elif (salBruto >= 3751.06 and salBruto <= 4664.68):
            IRRF = (salBruto * 0.225) - 636.13
        elif (salBruto > 4664.68):
            IRRF = (salBruto * 0.275) - 869,36

        salLiquido = (salBruto - (INSS + IRRF + outros))

        print(f'R${salLiquido} \n')

        folhaData = [salBruto, dependentes, outros, salLiquido]
        
        with open('folhaData.txt','r+') as arquivo:
            for valor in arquivo:
                print(valor)
            arquivo.write(str(folhaData) + '\n')

        return salLiquido
    
    opcao = ''
    while (opcao != 0):
        opcao = int(input('O que deseja acessar?\n1 - Gastos\n2 - Lucros\n3 - Faturamento\n\nFolha de Pagamento\n4 - Salário Funcionários\n0 - Retornar\n'))
        if (opcao == 1):
            os.system('cls')
            switch(opcao)
        elif (opcao == 2):
            os.system('cls')
            switch(opcao)
        elif (opcao == 3):
            os.system('cls')
            switch(opcao)
        elif (opcao == 4):
            os.system('cls')
            folhaPag()
        elif (opcao == 0):
            os.system('cls')
            break
