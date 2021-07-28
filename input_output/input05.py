name = "Tomas"
age = 10
a = 0.1234567890123456789
fmt_string = "String: {0}, Integer Number: {1}, Floating Number: {2}"
print(fmt_string.format(name, age, a))

a = 0.1234567890123456789
print("{0: .2f}, {0:.5f}".format(a))