class Atm:
    def __init__(self,pin):
        self.pin = pin

    def check_balance(self):
        print("Your balance is :-")
        print("150")

    def withdrawl1(self,withdrawn):
        new_amount = 150 - withdrawn
        print("You have withdrawn amount "+str(withdrawn) + ". Your remaining balance is "+ str(new_amount))
    
    def withdrawl2(self,Add):
        new_amount = 150 + Add
        print("You have Add amount "+str(Add) + ". Your remaining balance is "+ str(new_amount))


def main():
    print("Welcome to Tech Bank!")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Withdraw")
        print("2. Add Amount")
        choose = int(input(": "))
        if (choose == 1):
           Amount = int(input("Enter the amount:- "))
           new_user.withdrawl1(Amount)
        if(choose==2):
            Amount = int(input("Enter the amount:- "))
            new_user.withdrawl2(Amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()