from ValidacaoEmail import ValidateEmail
from ValidacaoCPF import ValidateCpf
from ValidacaoCNPJ import ValidateCNPJ


escolha = input('escolha o que deseja ser validado\n (A)Validação de E-mail\n (B)Validação de CPF\n (C)Validação de CNPJ\n (S)Sair\n ')

if escolha == 'A':
    ValidateEmail()

elif escolha == 'B':
    cpf = str(input("digite seu cpf:\n ")).replace('.','').replace('-','')
    ValidateCpf(cpf)

elif escolha == 'C':
    ValidateCNPJ()
        
else:
    print('finalizando programa...')
