import math
import os
import time
import datetime
import math
import random
import secrets

shoppinglist = []
totalprice = []


class Products(object):

    def __init__(self, price, quantityavail, description, delivery):
        self.price = price
        self.quantityavail = quantityavail
        self.description = description
        self.delivery = delivery

    class ShoppingCart(object):

        def __init__(self):
            super().__init__()
            self.shoppinglist = []
            self.adding = True

        def getlist(self):
            items = 'Cart Items: \n'
            for item in self.shoppinglist:
                items += item + "\n"
            return items

    def buy(self):

        while self.quantityavail == 0:
            print('Sorry, this item is out of stock'.format(self.description))
            return
        while self.quantityavail > 0:
            us = input("Would you like to add to cart?")
            if us == "Yes":
                print("How many items would you like? We have {} in stock".format(self.quantityavail))
                quant = int(input("Amount:  "))
                if quant > self.quantityavail:
                    print('Sorry, we only have {} left'.format(self.quantityavail))

                elif quant < self.quantityavail:
                    self.quantityavail = self.quantityavail - quant
                    subto = self.price * quant
                    total = subto
                    totalprice.append(total)
                    print("There are now {} left".format(self.quantityavail))
                    global userinp
                    global shoppinglist
                    shoppinglist.append(userinp)
                    print("The following items are in your cart, with a cost of:", sum(totalprice), shoppinglist, quant,
                          "items")
                    mm = input("Would you like to add more items?")
                    if mm == "No":
                        print("The total price is:", sum(totalprice), shoppinglist)
                        print("The delivery options available are:{} \n Enter 1 for Courier \n Enter 2 for Post".format(
                            self.delivery))
                        delivery = int(input('Enter a number: '))
                        if delivery == 1:
                            print("The total cost is $", (sum(totalprice) + 25))
                            break
                        elif delivery == 2:
                            print("The total cost is :$", (sum(totalprice) + 5))
                            break
                        else:
                            print("Error")
                            break

                    if mm == "Yes":
                        sb = input("Would you like to Search or Browse? \n Please enter the term exactly")
                        if sb == str("Search"):
                            search = input("Enter Search Term")
                            if search in stock:
                                print("Item Found!!")
                            else:
                                print("Item unavailable")

                        elif sb == str("Browse"):
                            print("Which item would you like to view? {}".format(','.join(stock.keys())))
                        else:
                            print("Error")

                        userinp = input("To order, Please enter the item name: ")
                        shoppinglist.append(userinp)
                        if userinp not in stock:
                            print("Sorry, this item is out of stock.".format(userinp))

                        stock[userinp].buy()




            elif us == "No":
                break
        else:
            print("Error")


stock = {}
stock['HP laptop'] = Products(2000, 10, "HP Laptop", "\n Courier 25 \n Post 5")
stock['Polo Shirt'] = Products(100, 25, "Polo Shirt", "Post 5")
stock['OnePlus Phone'] = Products(500, 20, "OnePlus Phone", "\n Courier 25 \n Post 5")

sb = input("Would you like to Search or Browse? \n Please enter the term exactly")
if sb == str("Search"):
    search = input("Enter Search Term")
    if search in stock:
        print("Item Found!!")
    else:
        print("Item unavailable")

elif sb == str("Browse"):
    print("Which item would you like to view? {}".format(','.join(stock.keys())))
else:
    print("Error")

userinp = input("To order, Please enter the item name: ")

if userinp not in stock:
    print("Sorry, this item is out of stock.".format(userinp))

stock[userinp].buy()


class Payment(object):

    def __init__(self, name):
        self.name = name

    def pay(self):
        if self.name == int:
            print('Sorry, this delivery option is unavailable'.format(self.name))
            return
        elif self.name == "Paypal":
            print("Please wait while we direct you to the PayPal Website".format(self.name))
            time.sleep(1)
            print("Redirecting to PayPal.com")
            time.sleep(1)
            print("Please complete payment")
            time.sleep(3)
            print("Payment Confirmed!, your order number is:", (secrets.token_hex(4)))
            print("Order completed, Thank you for your support")
            print("You may close this tab")
        elif self.name == "Bank Card":
            print("Please enter your card details")
            value = input("Card Number")
            while len(value) != 16:
                print("The Card number entered is not valid, Please contact customer care for assistance")
                break
            else:
                exp = input("Please enter card expiry details MMYY")
                if len(exp) != 4:
                    print("Incorrect expiry, Please try again")

                else:
                    cvv = input("Please enter your 3 digit CVV Number")
                    if len(cvv) != 3:
                        print("Incorrect CVV")
                    else:
                        print("Validating, please wait")
                        time.sleep(3)
                        print("Success")
                        print("Payment Confirmed!, your order number is:", (secrets.token_hex(4)))
                        print("Order completed, Thank you for your support")
                        print("You may close this tab")


        elif self.name == "Gift Voucher":
            print("Please enter your gift voucher number when prompted")
            value = input("Voucher Number")
            while len(value) != 10:
                print("The Voucher number entered is not valid, Please contact customer care for assistance")
                break
            else:
                print("Validating, Please wait")
                time.sleep(3)
                print("Success")
                print("Payment Confirmed!, your order number is:", (secrets.token_hex(4)))
                print("Order completed, Thank you for your support")
                print("You may close this tab")


paym = {}
paym['Paypal'] = Payment("Paypal")
paym['Bank Card'] = Payment("Bank Card")
paym['Gift Voucher'] = Payment("Gift Voucher")

print("Which payment method would you like to choose: {}".format(','.join(paym.keys())))
userinp = input("Please enter the payment name exactly: ")

if userinp not in paym:
    print("Sorry, this delivery option is unavailable".format(userinp))

paym[userinp].pay()
