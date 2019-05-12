#!/usr/bin/python3

print("""

  |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+

""")

fl = open("data.txt", "r")
fl.read()

if (fl.read() != ""):
  print("Hello I am some cat. I dont have name yet but you can name me!")
  print("Enter name you wish to name me: ")
  name = input()

  print("Thank you for this beautiful name! Enter my age now: ")
  old = input()

  if (float(old) > 15):
    print("Are you kidding me? Do you think that I am some old piece of shit? Try to google how old can I be!!!")
  else:
    pass

  def init():
    cat_name = name
    cat_old = old
    print("Ok have it - My name is " + cat_name + " and I am " + str(cat_old) + " years old.")
    wt = open("data.txt", "w")
    wt.write(cat_name)
    wt.write("\n")
    wt.write(cat_old)
    wt.close()

  def say_instructions():
    print("Everything what can I do is in different files. Try some of them!")
    print("Here is the list: catchMouse, generalInfo" + " type name of the file to run it: ")

    al = input()

    if (al == "catchMouse"):
      print("Run catchMouse.py")
    elif(al == "generalInfo"):
      print("Run generalInfo.py")
    else:
      pass

  init()
  say_instructions()

else:
  print("Hello, I am your cat! But you already were here!")
