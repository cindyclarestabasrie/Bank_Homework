from Bank.Banking import *
from Bank.Account_class import *

bni = Bank("BNI")

cindy = Customer("Cindy", "Basrie")
steph = Customer("Stephanie", "Basrie")
bni.customer = [["Cindy", "Basrie"], ["Stephanie", "Basrie"]]
customer_dict = {" ".join(bni.customer[0]): cindy, " ".join(bni.customer[1]): steph}

def main():
    while True:
        print("\nWelcome to BNI", end="")
        print("\n1. Bank Staff \n2. Customer Service \n3. Done")
        inp = input("Input: ")
        if inp == "1":
            while inp == "1":
                print("\n1. Get Customer""\n2. Number of Customers""\n3. Add Customer \n4. Return to main menu")
                a = input("Input: ")
                if a == "1":
                    while a == "1":
                        try:
                            b = int(input("\nInput Customer List Index: "))
                            print("\nCustomer:", bni.getCustomer(b-1), "\n")
                            print("1. Set Customer's Balance \n2. Get Customer's Balance \n3. Back")
                            c = input("Input: ")
                            if c == "1":
                                d = int(input("\nSet amount to be in the balance: "))
                                customer_dict[bni.getCustomer(b-1)].setAccount(d)
                                print("Balance is set to $" + str(customer_dict[bni.getCustomer(b-1)].getAccount()) + "\n")
                            elif c == "2":
                                try:
                                    print("Customer's Balance: $", customer_dict[bni.getCustomer(b-1)].getAccount())
                                except:
                                    print("Customer's balance has not been set yet.")
                            elif c == "3":
                                a = False
                        except:
                            print("Please input in integer.")
                            a = False

                elif a == "2":
                    print("\nNumber of Customers in Bank: ", bni.getNumOfCustomer())
                elif a == "3":
                    b = input("Input Customer's First Name: ")
                    c = input("Input Customer's Last Name: ")
                    bni.addCustomer(b.capitalize(), c.capitalize())
                    new = Customer(b.capitalize(), c.capitalize())
                    customer_dict[" ".join(bni.customer[-1])] = new
                elif a == "4":
                    print("Returning to Main Menu.\n")
                    inp = False

        elif inp == "2":
            a = input("Input your First Name: ")
            b = input("Input your Last Name: ")
            c = a.capitalize() + " " + b.capitalize()
            if c.split(" ") in bni.customer:
                print("\nWelcome, " + " ".join(bni.customer[bni.customer.index(c.split(" "))]) + "!")
                while inp == "2":
                    print("1. Get Balance \n2. Transaction \n3. Return to Main Menu")
                    d = input("Input: ")
                    if d == "1":
                        try:
                            print("\nYour Balance: $" + str(customer_dict[c].getAccount()))
                        except:
                            print("\nYou have not set your balance. Go to Bank Staff and set your balance first.\n")

                    elif d == "2":
                        while d == "2":
                            print("\n1. Deposit""\n2. Withdraw""\n3. Transfer \n4. Back")
                            e = input("Input: ")
                            if e == "1":
                                try:
                                    f = int(input("\nInput amount to deposit: "))
                                    Account.deposit(customer_dict[c], f)
                                except:
                                    print("You haven't set your balance. "
                                          "Please go to Bank Staff and set your balance there.\n")
                            elif e == "2":
                                f = int(input("\nInput amount to withdraw: "))
                                Account.withdraw(customer_dict[c], f)
                            elif e == "3":
                                while e == "3":
                                    f = input("\nTransfer to which account?\nInput First Name: ")
                                    g = input("Input Last Name: ")
                                    h = f.capitalize() + " " + g.capitalize()
                                    if h in customer_dict:
                                        try:
                                            j = int(input("Input amount to transfer: "))
                                            Account.transfer(customer_dict[c], customer_dict[h], j)
                                            print("Your balance: $", customer_dict[c].getAccount())
                                            e = False
                                        except:
                                            print("Error in transaction. The other account's balance is not set yet.\n")
                                    else:
                                        print("The account you are trying to transfer to does not exist.\n")
                            elif e == "4":
                                d = False
                    elif d == "3":
                        inp = False
            else:
                print("You don't have an account yet, go back to main menu "
                      "and choose Bank Staff to create a new account. \n")
        elif inp == "3":
            break
main()
