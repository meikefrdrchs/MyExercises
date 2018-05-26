Last login: Tue May 22 14:20:41 on ttys000
Meikes-MacBook-Air:~ Meike$ cd Downloads
Meikes-MacBook-Air:Downloads Meike$ mkdir tb1Sessions/

Meikes-MacBook-Air:Downloads Meike$ cd tb1Sessions
Meikes-MacBook-Air:tb1Sessions Meike$ atom 2018_05_22
Meikes-MacBook-Air:tb1Sessions Meike$ conda install jupyter

Meikes-MacBook-Air:tb1Sessions Meike$ cd ..
Meikes-MacBook-Air:Downloads Meike$ python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:14:23)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.



>>> print ("Hello World")
Hello World
>>> def greet():
...     print("Hello World")
...
>>> greet()
Hello World
>>> def greet(firstname):
...     print("Hello"+firstname)
...
>>> greet("490329")
Hello490329
>>> def greet(firstname):
...     print("Hello",firstname)
...
>>> greet("Meike")
Hello Meike
>>>

>>> def greet(firstname):
     print("Hello",firstname*10)


greet("Meike")
Hello MeikeMeikeMeikeMeikeMeikeMeikeMeikeMeikeMeikeMeike
print("ha"*10)
hahahahahahahahahaha




myName = "Meike Friedrichs"

myName.split(" ")

myList = myName.split(" ")

myList[0]

first_name = myList[0]

first_name

myName.replace("e","ü")

myName1 = myName.replace("e","3")

myName.lower()
myName.upper()
myName.capitalize()

myName.strip() (removes space after element)





Last login: Sat May 26 20:54:33 on ttys000
Meikes-Air:~ Meike$ cd MyExercises/
Meikes-Air:MyExercises Meike$ ls
Readme.txt
Meikes-Air:MyExercises Meike$ git

Meikes-Air:MyExercises Meike$ git status
On branch master
nothing to commit, working tree clean

Meikes-Air:MyExercises Meike$ git log
commit 68655bff585121169fa42167045c72c8992ba75c (HEAD -> master)
Author: meikefrdrchs <friedrichs.meike@web.de>
Date:   Sat May 26 20:54:55 2018 +0200

    first commit
