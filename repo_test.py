print("this is a test")

print("welcome to the COM411!")


print("Welcome to the show!")

firstNumber = 12
secondNumber = 40

if firstNumber>secondNumber:
    print("First is bigger")
elif firstNumber<secondNumber:
    print("First is smaller")
else:
    print("Both are equal")

print("Done!")

print("What type of book is this")
books = str(input())

if books == "adventure":
    print("I like adventure books!")


print("Have finished reading books")

print("Please enter the activity to be performed")
activity = str(input())

if activity =="calculate":
    print("Performing calculations...")

print("Activity completed")


print("Please enter a whole number.")
number = int(input())


if number % 2 == 0:


    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")

print("Please enter the first whole number?")
firstnumber1 = int(input())

print("Please enter the second whole number?")
secondnumber2 = int(input())

print("Please enter the third whole number?")
third_number3 = int(input())

even_numbers = 0
odd_numbers = 0


if firstnumber1 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    oddnumbers = odd_numbers + 1

if secondnumber2 % 2 == 0:
    evennumbers = even_numbers + 1
else:
    oddnumbers = odd_numbers + 1

if third_number3 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

print(f"There were {even_numbers} even and {odd_numbers} odd numbers")

print("what type of cover does the book have? ")
cover = input()
if cover == "soft":
    print("the book cover is soft")
perfect_bound = input()

if perfect_bound =="yes":
    print("soft cover is perfect bound")

else :
    print("soft cover,perfect bound  books are very popular!")

print("where should i look in the bedroom")
place = input()

if place=="in the bedroom":
    print("where in the bedroom  should i look?")

    place = input()










