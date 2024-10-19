import customerFundTransfer
def customerBankDetails(name, card,balance):
    #print("Enter balance", balance)                    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Fund Transfer")
        print("5. Exit")
        choice = int(input("Enter choice"))
        if choice == 1:
            amount=int(input("Enter Amount : "))
            balance=balance+amount
            print("You current balance is ",balance)
        elif choice==2:
            amount=int(input("Enter Amount : "))
            if balance<amount:
                print("Insufficient Balance")
            else:
                balance=balance-amount
                print("You current balance is ",balance)
        elif choice==3:
            print("You current balance is ",balance)
        elif choice==4:
            customerFundTransfer.fundTransfer(name, card, balance)
        elif choice==5:
            break
    else:
        print("Invalid Input")
            

    
        