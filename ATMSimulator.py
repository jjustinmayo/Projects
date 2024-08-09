# cashh on hand

# Total balance on account

# deposit, withdraw, check balance, exit


total_balance = 2500

cash_on_hand = 1000

def dollar_change(action, amount, total_balance, cash_on_hand):
    if action == "D":
        total_balance += amount
        cash_on_hand -= amount
    elif action == "W":
        total_balance -= amount
        cash_on_hand += amount
        
check = input("Insert your card? (Y/N): ").upper()

if check == "Y":
    print("total balance: $", total_balance)
    print("cash on hand: $", cash_on_hand)
    print("Menu:")
    print("'D' for Deposit")
    print("'W' for Withdraw")
    print("'C' for Check Balance")
    print("'E' for Exit")
    action = input("Enter action: ").upper()
    if action == "D":
        amount = int(input("Deposit Amount: "))
        if (cash_on_hand > 0 and amount <= cash_on_hand):
            dollar_change(action, amount, total_balance, cash_on_hand)
            print("New balance ", total_balance)
            print("Total cash on hand: ", cash_on_hand)
            input("Make another transaction") 
        else: 
            print("Insufficient funds")
    elif action == "W":
        amount = int(input("Withdraw Amount: "))
    elif action == "C":
        print("Current Balance: $", total_balance)
    else:
        print("Goodbye")        
else: 
    print("Goodbye")
    
    

        




    
    