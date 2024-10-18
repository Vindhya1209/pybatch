import customerDetails

while True:
    customer =[{
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
    print("*** WELCOME TO HDFC***")
    card = (input("Enter Card Number : "))
    
    for i in customer:
        if card == i['card']:
            attempts = 0
            while attempts < 3:
                pin = input("Enter Pin : ")
                if pin == i['pin']:
                    print("Welcome", i['name'])
                    balance =  i['balance']
                    customerDetails.customerBankDetails(balance)
                    break
                    
                else:   
                    attempts = attempts + 1
                    print("Invalid pin")   
                     
            else:
                print("You have exceeded the attempts, Please try after some time")         
                break   
    else:
        print("Invalid Card Number, Please try again")
                    