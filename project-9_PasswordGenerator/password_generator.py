import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols=['!','&','#','$','%','(',')','*','+']

print("Welcome to Password Generator!")
n_letters=int(input("How many letters you want in your password: "))
n_numbers=int(input("How many numbers you want in your password: "))
n_symbols=int(input("How many symbols you want in your password: "))

password_list=[]
password=""

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char

for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    password_list+=num

for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password_list+=sym

random.shuffle(password_list)

for char in password_list:
    password+=char

print("Password: ",password)