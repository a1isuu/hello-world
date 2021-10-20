import re
def ValidacaoEmail():
    email = str(input("Insira o endereço de email: "))
    tag = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
  
    if tag:
            print("O email %s teve sua validade comprovada. " %email)
    else:
            print("O email %s não é válido! " %email)
    email()