import customerDetails
import random as r

while True:
    customer = [{
        "name": "John",
        "card": "1111",
        "pin": "1234",
        "balance": 3000,
    },
    {
        "name": "Cathy",
        "card": "2222",
        "pin": "4321",
        "balance": 6000,
    }]
    
    print("*** WELCOME TO HDFC ***")
    print("1. Existing Customer")
    print("2. New Customer")

    exist = int(input())

    if exist != 1:
        # New customer creation
        newCustomerName = input("Please enter your Name: ")
        newCustomerCard = str(r.randint(1111, 9999))
        newCustomerPin = str(r.randint(1111, 9999))
        newCustomerBalance = 1000
        customer.append({
            "name": newCustomerName, 
            "card": newCustomerCard, 
            "pin": newCustomerPin, 
            "balance": newCustomerBalance
        })
        print(f"Congratulations {newCustomerName}, You have created an account and your card details are:")
        print(f"Card: {newCustomerCard}\nPin: {newCustomerPin}\nBalance: {newCustomerBalance}")
        
        # Automatically set the new customer card for login
        card = newCustomerCard
        print("\nProceeding to login...\n")
    else:
        # Existing customer login
        card = input("Enter Card Number: ")

    # The login block, now used for both new and existing customers
    for i in customer:
        if card == i['card']:
            attempts = 0
            while attempts < 3:
                pin = input("Enter Pin: ")
                if pin == i['pin']:
                    print("Welcome", i['name'])
                    balance = i['balance']
                    name = i["name"]
                    customerDetails.customerBankDetails(name, card,balance)
                    break
                else:
                    attempts += 1
                    print("Invalid pin")   
            else:
                print("You have exceeded the attempts, Please try after some time")
            break
    else:
        print("Invalid Card Number, Please try again")
