from clearAndLoading import Loading, Typing
from getpass import getpass
from time import sleep
import random
import sys


# stored all the customer data in here
account_pin = {}
account_balance = {}
account_number = {}
# ( I use dictionary for handle the customer data )

# loading animation object
clearLoad = Loading(0, 3, 0.3)


# all of the function that we use in this program

def welcome():
    
    # call a loading animation
    clearLoad.loadingAnimation()

    message = """
                        Welcome to E-Banking System

                                (1) Sign Up
                                (2) Login
                                (3) Exit
    
        (if you have made an account, then just login again please. Thank You)
    
    
                                    >>> """
    choice = input(message)

    # condition
    if choice == "1" or choice.lower() == "sign up":
        # goes to the sign_up function
        sign_up()
    elif choice == "2" or choice.lower() == "login":
        # goes to the login function
        login()
    elif choice == "3" or choice.lower() == "exit":
        # goes to the exit_program function
        exit_program()
    elif choice == "kopinya enak banget":
        secret_password()
    else:
        print("\n\n\t\t\t\tInvalid Input !")
        # sleep time
        sleep(2)

        # return to the welcome function
        welcome()


def secret_password():
    clearLoad.clear()

    pw = getpass(prompt="Secret Pass >> ")
    
    if pw == "hahahihihuhu":
        clearLoad.loadingAnimation()

        for keyPin, keyBalance, keyNumber in zip(account_pin, account_balance, account_number):
            message = f"""
                        {keyPin}:
                        - Pin = {account_pin[keyPin]}
                        - Balance = $ {account_balance[keyBalance]}
                        - Number = {account_number[keyNumber]}"""
            print(message)
            # if the output was nothing, then the dictionary is empty (no data has been input)

        input("\n\n\t\t\t *press ENTER for return")

        # return to the previous function
        welcome()
    else:
        print("\nWrong Password !")
        
        sleep(1)
        return welcome()


def exit_program():
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(0.5)

    # exit message
    message = """\n\n\n\n\n\n\n\n\n\t\t\t\tThanks For Coming :) """
    retype = Typing(message, 5, 0.1, 0.3, False)

    # retype animation
    retype.typeAnimation()

    # exit the program
    sys.exit()


def sign_up():
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(0.5)

    # temporary container for customer number
    tmp_customer_number = []

    try:
        customer_name = input("\n\t\t Full Name >> ").upper()
        customer_pin = int(input("\n\t\t Bank Pin >> "))
        customer_balance = int(input("\n\t\t First Balance in your Bank Account >> $ "))

        sleep(1)

        if len(str(customer_pin)) != 6:
            warnMessage = """
            Pin must be a 6 digit number, and the first digit can't be a 0

                        *press ENTER for repeating the input
            """
            print(warnMessage)
            input()

            # return to the previous function
            sign_up()
        elif customer_balance < 5:
            warnMessage = """
                        You can't store your money below $5 !

                        *press ENTER for repeating the input
            """
            print(warnMessage)
            input()

            # return to the previous function
            sign_up()
        else:
            i = 10
            while i > 0:
                tmp_customer_number.append(str(random.randint(0, 9)))
                i -= 1
            # got the customer numbers
            customer_number = int("".join(tmp_customer_number))

            # store all the data to the dictionary
            account_pin[customer_name] = customer_pin
            account_number[customer_name] = customer_number
            account_balance[customer_name] = customer_balance

            sleep(1)
            
            # call a loading animation
            clearLoad.loadingAnimation()

            printData = f"""
                                   Account Data

                        - Name >> {customer_name.upper()}

                        - Account Number >> {customer_number}

                        - Main Balance >> ${customer_balance}
            
                                    
                              Data has been stored . . .

                            *press ENTER for continue
            """
            print(printData)
            input()

            # return to the previous function
            welcome()
    except ValueError:

        warnMessage = """
                    Your pin and balance must be an Integer and without a space !

                            *press ENTER for repeating the input
        """
        print(warnMessage)
        input()

        # return to the previous function
        sign_up()


def login():
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(0.5)

    login_name = input("\n\t\tEnter your Name: ").upper()
    login_pin = int(getpass(prompt="\n\t\tEnter your Account Pin: "))

    # check if the bank account is exist
    if login_name in account_pin.keys():
        if login_pin in account_pin.values():
            # open the account
            banking_choice(login_name)
        else:
            message = """

                            Your Pin is Wrong !


                *press ENTER for repeat, or make a new Account 
            """
            print(message)
            input()

            # return to the previous function
            welcome()
    else:
        message = """
                    
                           Your Name Doesn't Exist !


                *press ENTER for repeat, or make a new Account 
        """
        print(message)
        input()
        
        # return to the previous function
        welcome()


def banking_choice(login_name):
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(0.5)

    message = f"""
                                (1) Deposit
                                (2) Withdraw
                                (3) Check Balance
                                (4) Back
    
                                    >>> """
    choice = input(message)

    # condition
    if choice == "1" or choice.lower() == "deposit":
        deposit(login_name)
    elif choice == "2" or choice.lower() == "withdraw":
        withdraw(login_name)
    elif choice == "3" or choice.lower() == "check balance":
        check_balance(login_name)
    elif choice == "4" or choice.lower() == "back":
        welcome()
    else:
        message = """

                                Invalid Input !


                        *press ENTER for repeat the login
        """
        print(message)
        input()

        # return to the previous function
        login()


def last_choice(account_name):
    
    # call a loading animation
    clearLoad.loadingAnimation()
    
    message = """
                    Do you want to do another transaction? (Y / n)
    
                                    >>> """
    lastConfirmation = input(message)

    # condition
    if lastConfirmation.upper() == "Y":
        banking_choice(account_name)
    elif lastConfirmation.upper() == "N":
        welcome()
    else:
        print("\n\n\t\t\t\tInvalid Input !")

        sleep(2)
        # repeat the input
        last_choice(account_name)


def deposit(account_name):
    # (<-- REMAINING B-U-G -->)
    # I think there is a bug in this function, and I might fix it later.
 
    # The bug is, when we input the money balance that we wanna deposit with nothing, it will generate to the sign_up function ( what I want when this case is happen is, it will just back to the deposit() function again and just keep looping until there is a something that got inputted on it )

    # call a loading animation
    clearLoad.loadingAnimation()
    
    sleep(0.5)

    saveMoney = int(input("\n\t\tEnter the Money Balance that you want to save: $ "))
    
    if saveMoney >= 5:
        # update the money balance
        account_balance[account_name] += saveMoney
        
        sleep(1)

        message = f"""
        
                            Your Balance has been Updated

                                (Main Balance: ${account_balance[account_name]})


                            *press ENTER for continue
        """
        print(message)
        input()

        # last confirm
        last_choice(account_name)
    else:
        sleep(1)

        message = """
                        
                        The Minimum Balance that You can Store is $5


                                *press ENTER for continue
        """
        print(message)
        input()

        deposit(account_name)


def withdraw(account_name):
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(0.5)

    withdrawMoney = int(input("\n\tEnter the Money Balance that you want to withdraw it: $ "))


    if withdrawMoney >= 5:
        sleep(1)

        # condition
        if account_balance[account_name] - withdrawMoney < 5:
            message = """
                        You can't withdraw your money right now 
                Because if you doing it, your balance is become less than $5
                        
                BANK RULES: You must have minimum $5 balance in your account !


                                *press ENTER for continue
            """
            print(message)
            input()

            # last confirm
            last_choice(account_name)
        else:
            # update the Balance
            account_balance[account_name] -= withdrawMoney

            message = f"""
                Transaction Success. You withdraw ${withdrawMoney} from your Bank Account
            
                            (Main Balance: ${account_balance[account_name]})


                            *press ENTER for continue
            """
            print(message)
            input()

            # last confirm
            last_choice(account_name)
    else:
        sleep(1)

        message = """
                        
                        The Minimum Balance that You can Withdraw is $5


                                *press ENTER for repeat
        """
        print(message)
        input()

        withdraw(account_name)


def check_balance(account_name):
    
    # call a loading animation
    clearLoad.loadingAnimation()
    sleep(1.5)

    message = f"""
                                    Account

                        - Name: {account_name.upper()}
                        
                        - Balance: ${account_balance[account_name]}


                            *press ENTER for continue
    """
    print(message)
    input()

    # last confirm
    last_choice(account_name)


# start the program 
if __name__ == "__main__":
    welcome()