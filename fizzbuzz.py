# This program will tell you which numbers between 1 and 100 are divisble by the
# numbers that you input into it

print("Welcome to my version of Fizzbuzz! Here you can enter any 2 numbers\nand I\'ll tell you every number that is divisible by them between 1 and 100!\n")

num1 = 0
num2 = 0

while True:
    print("Please enter a number between 1 and 100\n")
    try:
        num1 = int(input(">>"))
    except ValueError:
        print("You entered a non integer input, please try again\n")
        continue
    else:
        break

while True:
    print("\nPlease enter another number between 1 and 100\n")
    try:
        num2 = int(input(">>"))
    except ValueError:
        print("You entered a non integer input, please try again\n")
        continue
    else:
        break


print("num1 is " + str(num1))
print("num2 is " + str(num2))

for i in range(1, 101):
    stri = str(i)
    if (i % num1 == 0 and i % num2 == 0):
        print(stri + " fizzbuzz")
    elif (i % num1 == 0):
        print(stri + " fizz")
    elif (i % num2 == 0):
        print(stri + " buzz")
    else:
        print(stri)
