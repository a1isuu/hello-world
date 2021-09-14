import re
    
def email():
    email = str(input("enter the mail address::"))
    match = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
  
    
    
    if match:
        print("valid email :::", match.group())

    else:
        print("not valid:::")

email()


#acesso em 14/09/2021 14:24
#https://www.ti-enxame.com/pt/python/como-verificar-se-ha-um-endereco-de-email-valido/941744810/

