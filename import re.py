#Alison, Baruc, Matthews
import re
    
def email():
    email = str(input("Insira o endereço de email: "))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
  
    if tag:
        print("O email %s teve sua validade comprovada. " %email)
    else:
        print("O email %s não é válido! " %email)

email()


#acesso em 14/09/2021 14:24. (REGEX)
#https://www.ti-enxame.com/pt/python/como-verificar-se-ha-um-endereco-de-email-valido/941744810/

