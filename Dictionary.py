
# Write a Python program that collects multiple types of data(name,age,height,& 
# student status) from user input, stores them in a dictionary, and then prints out
# the collected data

a = input("Please enter your name :")
b = int(input("How many years old are you? :"))
c = input("How tall are you? :")
d = input("Please enter student status :")

e = {"name":a, "age":b, "height":c, "student status":d}
print(e)
print(type(e))