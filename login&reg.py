print(''' \nPlease select an option \n
                reg for Register
                login for Login
                forget for Forget Password
                ''')
def begin():
  global option
  
option = input()

if(option!= "reg" and option!= "login" and option!= "forget"):
    begin()
    
def access(option):
  if(option == "reg"):
    register()
  elif(option == "login"):
    login()
  elif(option == "forget"):
    forget_pass()
    access(option)
import re
import csv

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pwd_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')


def check_mail(email):
    if re.fullmatch(email_regex, email):
      return True
    else:
      return False

def check_pass(passw):
    if 6 < len(passw) < 16 and re.fullmatch(pwd_regex, passw):
      return True
    else:
      return False

def search_empass(email, passw , mode = 'r', newline = ''):
    with open('register.csv', mode, newline = newline) as f:
        reader = csv.reader(f)
        for i in reader:
            if email == i[0] and passw == i[1]:
                return True
        return False

def search_pass(email, mode = 'r', newline = ''):
    with open('register.csv', mode, newline = newline) as f:
        reader = csv.reader(f)
        for i in reader:
            if email == i[0]:
                print('\nYour Given Password is '+ i[1])
                return True
        return False
       
def writing(email, passw , mode = 'a', newline = ''):
    with open('register.csv', mode, newline = newline) as f:
        writer = csv.writer(f)
        writer.writerow([email, passw])


def register():
    print('\nNew Registration\n')
    email = input('email id: ')
    if check_mail(email):
        password = input('password: ')
        if check_pass(password):
            writing(email, password)
            print('\nRegistration Successfully')
        else:
            print('\npassword should be a minimum of 8 characters long and use uppercase letters, lowercase letters, numbers, and symbols characters')
    else:
        print('\nPlease Enter Valid Username \nPlease Register Again')

def login():
    email = input('email id: ')
    auth  = False
    if check_mail(email):
        password = input('password: ')
        if check_pass(password):
            if search_empass(email, password):
                print ('\nLogin Successful')
            else:
                print('\nYou are not Registered. \nPlease Register')
                register()
        else:
            print('\nInvalid Password \nTry Again')
    else:
        print('\nInvalid Username \nTry Again')

def forget_pass():
    email = input('email id: ')
    if check_mail(email):
        if check_pass(email):
            print ('\nLogin Successfully')
        else:
            print('\nNo Such User')
            register()
    else:
        print('\nInvalid Username \nTry Again')

begin()
access(option)
