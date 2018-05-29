firstname = "Meike"
lastname = "Friedrichs"

def intro(firstname,lastname):
    print("Hello stranger, my name is",firstname,lastname+".")

intro(firstname,lastname)

def desc1():
    print("I'm working on my first python project for my Tech Basics class at university and I'm sort of confused about everything.")

def desc2():
    print("So please don't judge my poor python skills!")

def desc():
    desc1()
    desc2()

desc()

firstname = firstname.replace("e","3")
firstname = firstname.replace("i","1")
firstname = firstname.replace("m","w")

lastname = lastname.replace("e","3")
lastname = lastname.replace("i","1")
lastname = lastname.replace("d","0")
lastname = lastname.replace("s","9")

newname = firstname,lastname

alias = ''.join(newname)
alias = alias.lower()


print("I'm just trying out some functions and commands so: If I had to choose an alias, it would probably be",alias+"!")
