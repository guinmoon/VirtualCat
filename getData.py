#!/usr/bin/python3

from github import Github

print("""

  |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+

""")

print("I found all the vievs and clones you have on GitHub! Who doesnt love programmers? (everybody)")
print("Here they are.")

def get_repos():
    repo = g.get_repo("TomasRoj/OctopusLab-Library")
    contents = repo.get_clones_traffic()
    contents = repo.get_clones_traffic(per="week")
    print(contents)

get_repos()