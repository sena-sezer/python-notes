parrot = "Norwegian Blue"
#         012345678901234
print(parrot)
print(parrot[3]) #4th letter of parrot 0 1 2 3 oluyor.
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
#we win
#negative indexing
print()
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-14])
#we win

#Slicing
print(parrot[0:6]) #index 0 to but not including 6 alıyor
# yani Norweg
print(parrot[3:5])
print(parrot[0:9]) # print(parrot[:9]) aynı sonucu verir
print(parrot[10:14]) # print(parrot[10:]) Blue

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:]) # it begining from beginnig goes to end
#Slicing Negative numbers
print(parrot[-4:-2]) # you cannot go to backwards from the starting position
print(parrot[-4:12]) #Bl
print(parrot[-14:8])
# step in slice
#parrot = "Norwegian Blue"
#          012345678901234
print(parrot[0:6:2]) #Nre the slice starts at index position 0, it extends up but not including to 6, we step through the sequence in steps of 2.
print(parrot[0:6:3]) #Nw obj[start:stop:step]

number = "9,223,373,036,854,775,807"
print(number[::]) 