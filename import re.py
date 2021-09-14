import re
    
def email():
    email = str(input("enter the mail address::"))
    match = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)
  
    
    
    if match:
        print("valid email :::", match.group())

    else:
        print("not valid:::")

email()

