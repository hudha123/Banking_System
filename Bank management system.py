class Bank:
    def __init__(self):
        userid = input("Enter your user Id : ")
        password = input("Enter your password : ")

        users = ["id111" , "id222" , "id333" , "id444" , "id555"]
        userpassid  = ["id@111" , "id@222" , "id@333" , "id@444" , "id@5555"]

        if userid in users and password == userpassid[users.index(userid)]:
            print("succesfully login")

        else:
            print("Invalid userid and Password")
            exit("try again")

        self.balance = 0
        print("Welcome!")
    def choice(self):
        while True:
            print("1. DEPOSIT")
            print("2. WITHDRAW")
            print("3. BALANCE ENQUIRY")
            print("4. LOGOUT")

            choice=int(input("Enter your choice : "))

            if choice==1:
                amount=float(input("Enter deposited amount:"))
                self.balance+=amount
                print("Deposited Amount: ",amount)
                print("Current Balance : ",self.balance)

            elif choice==2:
                amount=float(input("Enter withdrawing amount : "))
                if self.balance>=amount:
                    self.balance-=amount
                    print("Withdrawing Amount : ",amount)
                    print("Current Balance : ",self.balance)
                else:
                    print("Insufficient Balance")

            elif choice==3:
                print("Available Balance : ",self.balance)

            elif choice==4:
                print("Logout Successfully")
                Account.__init__()


            else:
                print("Invalid choice")
Account=Bank()
Account.choice()

