#!/usr/bin/python3

import random

print("""

  |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+

""")

print("You want to catch some mouses right? So lets do it")

mouses = random.randint(0, 7)

print("When I was hunting I found " + str(mouses) + " mouses. Good right?")

days = mouses / 2

print("This number of mouses can feed me " + str(days) + " days. But dont forget, I still need water!")

def write():
    wt = open("data.txt", "w")
    wt.write(str(days))
    wt.close()

write()