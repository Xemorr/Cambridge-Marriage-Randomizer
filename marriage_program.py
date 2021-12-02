import random

class Person:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __repr__(self):
        return self.name + " is studying " + self.subject

people = []

while True:
    name = input("Enter the name of the next person in the group! Type exit once you have added everyone. ")
    if name == "exit":
        break
    subject = input("Enter the name of this person's subject! ")
    people.append(Person(name, subject))

print(people)

input("Randomizing marriages.. Press enter!")

if len(people) == 1:
    print("There are too few people in this group... exiting program!")
    quit

def check_marriage(marriage):
    subjects = [person.subject for person in marriage]
    worked = False
    for subject1 in subjects:
        for subject2 in subjects:
            if subject1 != subject2:
                    return True
    return False

while True:
    random.shuffle(people)
    marriages = []
    if len(people) % 2 == 1:
        marriages.append(people[:3])
        people = people[3:]

    for i in range(0, len(people), 2):
        marriages.append([people[i], people[i + 1]])

    worked = True
    for marriage in marriages:
        if not check_marriage(marriage):
            worked = False
    if worked:
        break

for marriage in marriages:
    print("Marriage:")
    for person in marriage:
       print(person.name)
    
        
        


    
