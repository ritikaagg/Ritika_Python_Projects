print("Welcome to your account. Insert you ATM card")
print(" 1. Balance \n", "2. Withdraw\n", "3. Deposit\n", "4. Quit")
while True:
    option = int(input("Enter option: "))
    balance=8000
    if option==1:
        print("Balance: Rs.", balance)
    if option==2:
        print("Balance: Rs.", balance)
        withdraw =int(input("Enter the withdrawl amount: Rs."))
        if withdraw>0:
            forwardBalance=(balance-withdraw)
            print("Forward Balance Rs.", forwardBalance)
        elif withdraw>balance:
            print("No sufficient funds in account")
        else:
            print("No withdrawal made")
    if option==3:
        print("Balance Rs.", balance)
        deposit=int(input("Enter deposit amount: Rs."))
        if deposit>0:
            forwardBalance = (balance+deposit)
            print("Forward Balance Rs.", forwardBalance)
        else:
            print("No deposit made")
    if option==4:
        break