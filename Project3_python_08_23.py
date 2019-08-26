# python-basics-weekly-3

### VERY nice work! Great comments, easy to read and follow. Well done!
###
### Showing the current balance as part of a deposit or with draw was a *really* nice touch!

## Create a bank program. # Ask account holder for account name and pin
print("Welcome to Bank of MandaniTech")
account_Name= input("Please enter the name on this account\n:  ")
account_pin= input("Please enter your account pin\n:")

#User enters an option from the given menu
user_Balance=0
mainMenu=0
### This menu isn't needed and makes 2 menus print when you first launch the program.
### As soon as first iteration of loop starts, you are going to display menu anyway.
# print(f'Enter from an option below:\n'
#                         f'1) Check balance\n'
#                         f'2) Add money to account\n'
#                         f'3) Withdraw money from account\n'
#                         f'4) Quit\n')

while(mainMenu !='4'):
    mainMenu =input(f'Hello,What will you like to do?\n'
                    f'1) Check balance\n'
                    f'2) Add money to account\n'
                    f'3) Withdraw money from account\n'
                    f'4) Quit\n')

## User Chooses 1 for Balance enquiry
    if(mainMenu=='1'):
        print(f"\n\n\n{account_Name}'s account has ${user_Balance} dollars\n\n\n"
              f'*****************************************')
## User Chooses 2 for to make a deposit

    elif(mainMenu=='2'):
        user_deposit =int(input("How much would you like to deposit today? $"))
        user_Balance=user_Balance+user_deposit
        print(f"\n\n\n{account_Name}'s new Balance is $ {user_Balance}\n\n\n"
              f"**********************************************")
## User Chooses 3 for money withdrawal
    elif(mainMenu=='3'):
        account_pin_match=input("What is your account pin?\n:")
        if (account_pin_match == account_pin):
            withdraw_amount=int(input(f"{account_Name}'s account balance is {user_Balance}\n"
                                  f"_______________________________________\n"
                                  f"How much monies would {account_Name} like to withdraw today? \n$"))
            if(withdraw_amount>user_Balance): ## check if user balance is enough to withdraw money
                print("\n\n\nInsufficient Funds\n"
                  "\n************************************\n")
            else:
                user_Balance=user_Balance-withdraw_amount ## deduct the user balance with money withdrawen and print new balance
                print(f"\nPlease collect your money . {account_Name}'s New account balance is ${user_Balance}"
                  f"\n**********************************************************")
        else:
            print("Wrong pin")













