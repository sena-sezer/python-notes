#There are seven sequence types: strings, bytes, lists, tuples, bytearrays, buffers, and range objects.
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

print ("hello " * 5)
print ("Hello " * (5 + 4))

today = "friday"
print("day" in today)    #true
print("fri" in today)   #true
print("thur" in today)  #false
print("parrot" in today)    #false