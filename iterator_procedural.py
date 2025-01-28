def swipeleft(somelist):
    for something in somelist:
        yield something

people = [1,2,3,4,5,6,7,8]
swipelefter = swipeleft(people)
for person in swipelefter:
    print(person)