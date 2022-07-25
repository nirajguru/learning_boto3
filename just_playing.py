
""" Convert import json

my_json = '{"Name": "Niraj", "Age": 40}'
y = json.loads(my_json)

print(type(y))
print(y["Name"])
print(type(my_json))
"""


"""
import json

my_list = ["apple", "bananas"]
my_list_json = json.dumps(my_list)
print(type(my_list_json))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""


"""
#Check if the string starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
"""

'''
x = 10
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Error")
else:
    print("No error")
finally:
    print("This will run no matter what")


if x < 100:
    raise Exception("x is less than 100")

'''

'''
x = 5
if type(x) == str:
    print("x is a string")
else:
    raise TypeError("x is not a string")
'''
'''
txt = "his name is {0}. {0} is {1} years old. This is year {year}"
try:
    print(txt.format("Niraj", 29, year=2022))
except SyntaxError:
    print("this is a syntax error")
'''

'''
lambda is a small anonymous function
x = lambda a, b: a*b
print(x(5,6))
'''

'''
f = open("git-deploy.sh")
#print(f.read())
print(f.readline())
f.close()
'''

'''
import os
try:
    f = open("demofile.txt", "x")
    f.write("Adding some content")
    print("Contents added")
except FileExistsError:
    print("file exists")
os.remove("demofile.txt")
'''
'''
import os
if os.path.exists("demofile.txt"):
    print("file exists")
else:
    print("file doesn't exist")
'''
'''

import matplotlib.pyplot as plt
import numpy as np

#print(matplotlib.__version__)
xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints, ypoints)
plt.show()
'''

'''
from datetime import datetime as date
#x = date.now()
#print(x.hour)

date_string = "2018/08/09"
my_date = date.strptime(date_string, '%Y/%m/%d')
print(my_date)
'''

class Person():
    def __init__(mysillyself, name, age):
        mysillyself.name = name
        mysillyself.age = age
        print(f"from main class {name}")
    def myfunc(mysillyself):
        print("hello my name is" + mysillyself.name)
p1 = Person("Niraj", 30)
p1.myfunc()
p1.name = "Hey"
p1.myfunc()
del p1.age


class Student(Person):
    def __init__(mysillyself, name, age, country):
        super().__init__(name, age)
        mysillyself.country = country
        mysillyself.country = "UK"

s1 = Student("Raj", 30, "Netherlands")
s2 = Student("Hey", 40, "France")

print(s1.country)
print(s2.country)

