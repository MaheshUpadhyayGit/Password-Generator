import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol =  ['!', '@', '#', '&','*','!','~','$']
digit = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome the password generator\n")
n_letter = int(input("How many letter you want to in your password\n"))
n_symbol = int(input("How many symbol you want to in your password\n"))
n_digit = int(input("How many digit you want to in your password\n"))

password_list = []
for i in range(1,n_letter+1):
    char = random.choice(letter)
    password_list += char
for i in range(1,n_symbol+1):
    char = random.choice(symbol)
    password_list += char
for i in range(1,n_digit+1):
    char = random.choice(digit)
    password_list += char

print(password_list)
random.shuffle(password_list)
print(tuple(password_list))
password=""
for i in password_list:
    password += i
print(password)
    