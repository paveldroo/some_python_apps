correct_password = 'python123'
name = input('Whats your name? ')
surname = input('Whats your surname? ')
password = input('Enter password: ')

while correct_password != password:
    password = input('Try again: ')

message = 'Password correct, {} {}! Welcome!'.format(name, surname)
print(message)