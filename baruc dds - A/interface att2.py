from ValidacaoEmail import ValidacaoEmail
from ValidacaoCPF import ValidacaoCPF
from ValidacaoCNPJ import ValidacaoCNPJ


escolha = input('escolha o que deseja ser validado\n (A)Validação de E-mail\n (B)Validação de CPF\n (C)Validação de CNPJ\n (S)Sair\n ')

if escolha == 'A':
    ValidacaoEmail()

elif escolha == 'B':
    ValidacaoCPF()

elif escolha == 'C':
    ValidacaoCNPJ()
        
else:
    print('finalizando programa...')
