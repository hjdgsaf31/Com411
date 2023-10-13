print("How many apples should I remove?")
apples_to_remove = int(input())


apples_removed = 0


print("How many apples are here? : ")

while apples_removed < apples_to_remove:
    print("Removed apple.")
    apples_removed = apples_removed + 1

obstacles_avoiding = 0

print("How many obstacles must i avoid? ")
obstacles_avoided = int(input())

while obstacles_avoiding<obstacles_avoided:
    print("Avoiding obstacles.")
    obstacles_avoiding = obstacles_avoiding + 1

print(f"{obstacles_avoided} obstacles avoided.")

print("How many bars should be charged? ")
bars_to_charged= int(input())

bars_charged = 0

while bars_charged<bars_to_charged:
    bars_charged += 1
    print(f"Charging: {'█'* bars_charged}")

print("Please enter a phrase: ")
enter_a_phrase = input()

print("How far are we from the target")
distance = int(input())

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("Target achieved!")

print("what word do you see")
users_word= str(input())


