mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total) 

###########################
index = "Ability is a poor man's wealth".find("W")
print(index)

########################
fruit = "banana"
letter = fruit[1]
print (letter)

##########################
mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2

#What is the output of the following Python program?
mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
total = 0
while a < 3:
    b = 0
    while b < 2:
        total += mylist[a][b]
        b += 1
    a += 1
print(total)


#What is the output of the following Python program?
index = "Ability is a poor man's wealth".find("w")
print(index)