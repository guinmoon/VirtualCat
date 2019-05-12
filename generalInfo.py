#!/usr/bin/python3

fl = open("data.txt", "r")
fl.read()

import random

print("""
  |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
""")

with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print("I have food for: " + last_line + " days.")
    print("\n")
    print("Do you have to give me water?")
    an = input()

    if (an == "yes"):
        water = random.randint(1, 24)
    else:
        water = 0

    if (water != 0):
        print("I have water for: " + str(water) + " days.")
        print("\n")
    else:
        print("I dont have any water bro! I am dying...")

    