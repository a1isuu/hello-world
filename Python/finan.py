
def Financeiro():
    opcaoFinan = str(input('O que gostaria de saber ?\n1 - Gastos\n2 - Lucro\n3 - Faturamento\n')) 
    def switch(escolha):
        opcaoFinan = ''
        if escolha == '1':
            opcaoFinan = "Gastos"
            gastos = int
            mediaDespesas = int(input('Insira a média de despesas no último mês: '))
            print('{0}$ foram gastos no último mês.' .format(mediaDespesas))
            vendasMes = int(input('Agora insira o valor ganho pelas vendas do último mês: '))
            print('{0}$ representam o valor ganho no último mês.' .format(vendasMes))
            gastos = mediaDespesas / vendasMes
            print('Os gastos no último mês foram em torno de {0}$ ' .format(gastos))   
        elif escolha == '2':
            opcaoFinan = "Lucro"
            lucro = int 
            margemLucro = int
            receitasTotais = int(input('Insira o faturamento obtido com as vendas: '))
            print('{0}$ de faturamento.' .format(receitasTotais))
            custos = int(input('Agora insira os custos para a execução do trabalho: '))
            print('{0}$ foram gastos para a conclusão do produto.' .format(custos))
            lucro = receitasTotais - custos
            margemLucro = lucro / receitasTotais
            print('Foi obtida uma margem de lucro de {0}%\ncom um lucro bruto final de {1}$' .format(margemLucro, lucro))
        elif escolha == '3':
            opcaoFinan = "Faturamento"
            faturamento = int 
            fatuLiq = int
            precoVenda = int(input('Insira o preço de venda da unidade produzida: '))
            print('{0}$ é o valor de cada unidade vendida.' .format(precoVenda))
            quantVendas = int(input('Agora insira a quantidade de unidades vendidas: '))
            print(quantVendas, 'unidades foram vendidas')
            faturamento = precoVenda * quantVendas
            print('{0}$ foram faturados com as vendas.' .format(faturamento))
            resposta = str(input('Gostaria de saber o faturamento líquido obtido nessas vendas? *(Selecione caso tenham ocorrido devoluções do produto ou se paga impostos)\nY - Para sim, N - Para não\n'))
            while (resposta != 'N') or (resposta != 'n'):
                if (resposta == 'N') or (resposta == 'n'):
                    break
                if (resposta == 'Y') or (resposta == 'y'):
                    deducVendas = int(input('Insira quantos itens da mesma unidade foram devolvidos: '))
                    print(deducVendas, 'itens dessa unidade foram devolvidos e/ou cancelados.')
                    impostos = int(input('Agora insira a porcentagem de impostos paga: '))
                    print('{0}%''de impostos aplicados ao calculo.' .format(impostos))
                    fatuLiq = (faturamento - deducVendas) - (impostos / 100)
                    print('{0}$ de faturamento líquido foram obtidos com as vendas' .format(fatuLiq))
                while (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                    if (resposta == 'Y') or (resposta == 'y') or (resposta == 'N') or (resposta == 'n'):
                        break
                    if (resposta != 'Y') or (resposta != 'y') or (resposta != 'N') or (resposta != 'n'):
                        resposta = input('Opção inválida, por favor insira Y ou N.\n')
            
    switch(opcaoFinan)

    #def folhaPag ():
    #folhaPag()   
Financeiro()
