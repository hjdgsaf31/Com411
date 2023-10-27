print("Program Started")

print("Please enter the character: ")

characters = input()
if len(characters) == 1:
    print(f"the ascending order for {characters} is {ord(characters)}")
else:
    print("a single character")

print("Program ended")

print("Program Started")
print("Please enter an ASCII code")

code = int(input())


if code >= 32 and code <= 126:
    characters = chr(code)
    print(f"The character represented by the ASCII code {code} is {characters}  ")

print("program ended")

print("Please enter your name")#
name =input()
print("Hello", name)

print("please enter your school")
schoolname = input()
print("this is " ,schoolname)

# nesting function




