
def NumerarCPF(cpf): 
    cpf_numerado = []
    for a in cpf:
        a= int(a)
        cpf_numerado.append(a)
    return cpf_numerado

def Quantidade(cpf):
    if len(cpf)<11 or len(cpf)>11:
        return False
    else:
        return True

def VerificacaoDigito(cpf):
    if Quantidade(cpf):
        return False 
    else:
        cpfNumerado = NumerarCPF(cpf)
        acumulador=0 
        resultado=0
        controlador=10
        for numeros in cpfNumerado[0:9]:
            resultado= numeroscontrolador
            acumulador+= resultado
            controlador= controlador-1 
        acumulador=acumulador10%11
        if acumulador ==10:
            acumulador=0
        if acumulador == cpfNumerado[9]:
            return True

        if Quantidade(cpf):
            return False
        else:
            cpfNumerado = NumerarCPF(cpf)
            acumulador2=0 
            resultado2=0
            controlador2=11
            for numeros2 in cpfNumerado[0:10]:
                resultado2= numeros2 * controlador2 
                acumulador2+= resultado2
                controlador2= controlador2 - 1 
            acumulador2=acumulador2 * 10 % 11
        if acumulador2 ==10:
            acumulador2=0
        if acumulador2 == cpfNumerado[10]:
            return True
        else:
            return False

def ValidateCpf(cpf):
    if Quantidade(cpf) and VerificacaoDigito(cpf):
        print('o Cpf é válido!')
    else:
        print('Cpf invalido')
