print('Python'.isalpha())
print('Ver. 3.x'.isalpha())

print('12345'.isdigit())
print('1234ased'.isdigit())

print('abc1234'.isalnum())
print(' abc1234'.isalnum())

print(' '.isspace())
print(' 1 '.isspace())

print('PYTHON'.isupper())
print('Python'.isupper())
print('python'.islower())
print('Python'.islower())

string1 = 'Python is powerful. PYTHON IS EASY TO LEARN.'
print(string1.lower())
print(string1.upper())

print('Python'.lower() == 'python'.lower())
print('Python'.upper() == 'Python'.upper())