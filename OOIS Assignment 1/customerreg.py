import os
import time
import datetime
import math
import random
import linecache
import json
import sqlite3



class User():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


    def customer(self):
            print("Customer Registration")

            import sqlite3
            conn = sqlite3.connect('testDB2.db')
            cursor = conn.cursor()

            s_name = input("Please type your Name")
            s_address = input("Please type your address")
            s_email = input("Please enter your email address")
            s_contact = input("Please enter your contact number")
            s_pcode = input("Please enter a six digit passcode".format(int))

            cursor.execute("""
            INSERT INTO Customers(name, address, email, contact, pcode)
            VALUES (?,?,?,?,?)
            """, (s_name, s_address, s_email, s_contact, s_pcode))
            conn.commit()
            print('Data entered successfully.')
            conn.close()
            if (conn):
                conn.close()
                print("\nThe SQLite connection is closed.")
                print("Your details have been successfully recorded")
                print("Thank you, please follow the link sent to your email address to complete registration")

User.customer("self")