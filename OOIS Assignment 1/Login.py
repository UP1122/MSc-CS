import os
import time
import datetime
import math
import random
import linecache
import json

stock1 = {"HP laptop": {"Price": 2000, "Quantity": 10, "Delivery": True},
          "Polo Shirt": {"Price": 100, "Quantity": 25, "Delivery": False},
          "OnePlus Phone": {"Price": 500, "Quantity": 20, "Delivery": True}}


class Startpage():

        print("Welcome to UP stores \n 1= Customer Registration \n 2= Customer Login \n "
              "3= Third Party Seller Registration \n 4= Third Party Seller Login \n 5= Administrator Login")
        startpagechoice = input("Please select an option")


        if startpagechoice == "1":
            os.system("python customerreg.py")

        elif startpagechoice== "2":
            print("Login")
            input("Please enter your email address")
            input("Please enter your password")
            print("Login Successful!! Please wait while we redirect you to the site")
            time.sleep(3)
            os.system("python Ordering.py")

        elif startpagechoice == "3":
            print("Welcome to our 3rd party registration page \n Kindly complete the following:")

        elif startpagechoice == "4":
            print("Welcome to our 3rd party login page")

        elif startpagechoice == "5":

            print("Welcome to the Administration Page")

        else:
            print("You have entered an incorrect option, kindly return to the main page and select option 1-5")




