import random
import time

start = input("Would you like a new password?(yes/no)")

if start == "yes":
    print("Great, lets start!")
    print("One second!")
    print("..........................................................................................")

if start == "no":
    print("okay, see you again soon when you are needing a new password!")

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "/.,`;'\][=-!@£$%^&*(_+)<?>:|"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)







    

    



