
tables_list = ["Argentina" ,"Mexico" ,"Indian" ,"Japanese"]

tables_list.append("Chinese")


def directions():
    steps = ["move forward", "move backward", "Turn left", "Turn right"]
    return steps


def run_task1():
    print(directions())


run_task1()


list_offruits= ["apple",5,"banana",10,"cherry",15]
list_offruits[1] = "berry"

del list_offruits[4]
list_offruits.append("plum")
print(list_offruits)
print(list_offruits[1])


def movements():
    list_offnames =["move forward",10,"move backward",5,"move left",3,"move right",1]
    return list_offnames

def run_task2():
    steps = movements()
    print("moving...")

    for i in range(0, len(steps), 2):
        print(f"{steps[i]} for {steps[i+1]} steps")

run_task2()


def directions():
    steps1= ["move forward", "move backward", "turn left", "turn right"]
    return steps1
def menu_and_input():
    print("Please select a direction")
    dirs= directions()


temperatures = (19,23,21,21,20,18,22)
all_temperatures = temperatures + (20,21)
print(all_temperatures)
print(temperatures* 2)

print(20 in temperatures)




























