account={}
def creat_ac():
    print("You are creating a account")
    username=input("Enter your username you want to create:")
    if username in account:
      print(f"{username} already there")
      login_ac()
    else:
      password=input("Please create  a strong password:")
      account[username]={"password":password, "balance":0}
      print("Congratulations that you have created a account in Coders banks")
      print("now you can access the banking servies of the bank")
      bankingdetails(username)

def login_ac():
    username=input("Enter your Username:")
    password=input("Enter your account Password:")

    if username in account and account[username ]['password']==password:
      print(f"We welcome you again:{username}")
      bankingdetails(username)
    
    else:
      print("You are not a part of coders bank")
      print("First create your account")
      creat_ac()

def bankingdetails(username):
  while True:
    print("--Coders Bank Services--")
    print("1.Deposit cash")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.EXIT")
    choice=input("Enter the choice between 1 to 4:")

    if choice=='1':
     amount=int(input("Enter the amount you want to Deposit:"))
     if amount>0:
        account[username]['balance']+=amount
        print(f"deposited {amount} successfully")
     else:
       print("Invalid entry")

    elif choice=='2':
     amount=int(input("Enter the amount you want to withdraw:"))
     if amount > account[username]['balance']:
       print("Insufficient balance")
     elif amount <=0 :
       print("wrong entry")
     else:
       account[username]['balance']-=amount
       print(f"{amount} withdraw successfullly...")
    
    elif choice=='3':
     balance=account[username]['balance']
     print(f"{balance} in your account...")
    
    elif choice=='4':
     print("exit successfully..")
     print("Thank you for visiting us...")
     break
    
    else:
      print("Invalid entry choose betweeen 1 to 4")



while True:
   print("**Coders Bank**")
   print("1.Creates Account")
   print("2.Login Account")
   print("3.Exit")

   choice= input("enter choice beetwwen 1 to 3:")
   if choice=='1':
      creat_ac()
   elif choice=='2':
    login_ac()
   elif choice=="3":
    print("Thank you for visiting us")
    print("please  visting us again")
    break
   else:
    print("Invalid entry choose betweeen 1 to 3")








