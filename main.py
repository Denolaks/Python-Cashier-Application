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

letters = 1,2,3,4,5,6,7,8,9,0

while True:
    os.system("cls")
    option = input("-----DeHook Shopping Tools-----\nWhat you want to do?\n1 - Check Price\n2 - Sell Item\n3 - Check all items with prices.\n----------\n>>")

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

            print(f"\nYou should give {usermoney - price} to he/she.\n----------")
            with open("history.txt", "w") as f:
                f.writelines(f"Someone bought {itemname} for {price} at {datetime.now()}\n")
            input("Press key to continue.")
        else:
            print("\nInvalid Item Data. Please check All items.\n")
            input("Press key to continue.")

    if option == "3":
        for item, value in Prices.items():
            print(f"{item}, {value}₺\n")
            sleep(0.2)
        input("Press key to continue.")
