print("Today is a good dat yo learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in string')
print("hello" + " world")
greeting = "Hello"
#name = input("Please enter your name ")
# input dersem klavyeden girilibilir string ekliyorum
name = "Sena"
print(greeting + ' ' + name)
age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = " 2 years old"
print(name + f"is  {age} years old")

print(type(age))
#burada age'in typeini değiştirdik Javada falan bu olmuyordu.
#Python 3 numeric data types: int, float, complex
# integer: whole numbers (tam sayılar), have no limit float: real numbers, have fractional part, kesirli, ondalık vs.
print(f"Pi is approx {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approx {pi:12.50f}") #f strings