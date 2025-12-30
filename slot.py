import random
import time

amount = 0

def balance():
    print(amount)

def add():
    global amount
    money = int(input("Enter money to add to your account: "))
    if money <= 0:
        print("enter a valid number")
    else :
        amount = amount + money
        print(f"You deposited {money} in your account\n")


def widraw():
    global amount
    money = int(input("Enter money to widraw from your account: "))
    if money > amount:
        print("You dont have enough money")
    else :
        amount = amount - money

def rules():
    print("Welcome to the Slot Machine!")
    print("----------------------------")
    print("The rules are simple:")
    print("• There are 5 fruits in the machine.")
    print("• If all 3 symbols are different → You lose your bet.")
    print("• If any 2 symbols match → You win 1.5x your bet.")
    print("• If all 3 symbols match → You win 3x your bet.")
    print("----------------------------")




itemes = ("add money", "widraw", "balance", "play", "rules")
while True:


    for i,item in enumerate(itemes, start=1):
        print(i, item)

    print("-----------------------------")
    print("   welcome to slot machine   ")
    print("        🍊", "🍉", "🥭      ")
    print("-----------------------------")

    choice = input("Enter the task in (1/2/3/4/5): ")
    if choice == "1":
        add()
    elif choice == "2":
        widraw()
    elif choice == "3":
        balance()
    elif choice == "4":
        while True:
            a = random.choice(["🍊", "🍉", "🥭", "🍌", "🍎"])
            b = random.choice(["🍊", "🍉", "🥭", "🍌", "🍎"])
            c = random.choice(["🍊", "🍉", "🥭", "🍌", "🍎"])
            print(f"your balance is {amount}")
            ask = input("\nEnter the bet amount or q to quit: ")
            if ask.isdigit():
                ask = int(ask)
                if ask > amount:
                    print("You dont have enough money")
                    break
                else:
                    i = a, b , c
                    for l in i:
                        print(l, end = " ")
                        time.sleep(1)
                    amount = amount - ask

                    if a==b==c:
                        total = ask * 3
                        amount += total
                        print(f"you won {total} ")

                    elif a==b or a==c or b==c:
                        total = ask * 1.5
                        amount += total

                        print(f"you won {total} ")
                    else:
                        print("Try again")


            elif ask == "q":
                break
            else:
                print("Enter a valid number")
    elif choice == "5":
        rules()
    else:
        print("Enter a valid number")