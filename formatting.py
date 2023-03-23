for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i ** 3))
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i ** 3)) #left alligned > right alligned, ^centered

print()
print("Pi is approx {0:12}".format(22 / 7))
print("Pi is approx {0:12f}".format(22 / 7))
print("Pi is approx {0:12.50f}".format(22 / 7)) # sayının önüne boşluk ekliyor
print("Pi is approx {0:52.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))
print("Pi is approx {0:<72.54f}".format(22 / 7))
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i ** 3)) #left alligned > right alligned, ^centered
#4 haneli yer ayırıyor sonda
