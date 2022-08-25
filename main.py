from operator import contains
import os
from time import sleep
from datetime import datetime

#Add items like
# "Item Name": Price,
Prices = {
    "Kıymalı Börek": 20,
    "Patatesli Börek": 15,
    "Peynirli Börek": 15,
    "Ispanaklı Boyoz": 5,
    "Patatesli Poğaça": 5,
    "Çay": 4,
    "Kola": 9
}

while True:

    Money = open("MoneyHistory.txt", "r")
    #For clear the console.
    os.system("cls")

    option = input("-----DeHook Shopping Tools-----\nWhat you want to do?\n1 - Check Price\n2 - Sell Item\n3 - Check all items with prices.\n4 - Check History\n5 - Show Money History That You Earned\n----------\n>>")

    if option == "1":
        mainitem = ""
        itemname = input("----------\nEnter item name: ")
        if Prices.__contains__(itemname) == True:
            mainitem = Prices[itemname]
            print(f"{itemname}'s price is {mainitem}\n----------")
            input("Press key to continue.")
        else:
            print("\nInvalid Item Data. Please check All items.\n")
            input("Press key to continue.")

    if option == "2":
        usermoney = int(input("How much did he/she gave you?: "))
        mainitem = ""
        itemname = input("----------\nWhat he/she buy: ")
        if Prices.__contains__(itemname) == True:
            mainitem = Prices[itemname]
            price = mainitem

            History = open('history.txt', 'a')
            Money = open('MoneyHistory.txt', 'a')
            print(f"\nYou should give {usermoney - price} to he/she.\n----------")
            History.write(f"Someone bought {itemname} for {price} at {datetime.now()}\n")
            Money.write(f"Earned: {price} at {datetime.now()}\n")
            input("Press key to continue.")
        else:
            print("\nInvalid Item Data. Please check All items.\n")
            input("Press key to continue.")

    if option == "3":
        for item, value in Prices.items():
            print(f"{item}, {value}₺\n")
            sleep(0.2)
        input("Press key to continue.")

    if option == "4":

        History = open('history.txt', 'r')
        print(f"----------\nHistory:\n{History.read()}")
        input("Press key to continue.")

    if option == "5":
        Money = open("MoneyHistory.txt","r")

        count = 0
        Lines = Money.readlines()

        for line in Lines:
            count += 1
            moneyvals = line.strip()
            print(moneyvals)
        input("Press key to continue.")
