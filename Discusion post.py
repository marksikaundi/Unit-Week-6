#In python programming value objects are identical to variables in that they are used for testing identity of objects based on the value. Is operator is used to test and identity the object identity. Implementation of variables can reuse a single instance of an object.
#In Equivalence, value of objects can change within the scope of a mutable list while variables represent the relations between the objects. An object contains both value and identity which is identical to a variable that contains data of the object.
#The scope of an immutable object can not be changed. Is operator is used for objects that are identical while === is used for objects that have an equivalence. The operator is returns true if objects pointing to the same object are identical.


a1 = [100, 400, 600, 800]
a2 = [10, 40, 60, 80]

print(a1 == a2)
# Example 2 returns False since they are not same.

s1 = "Sony"
s2 = "Sony"

print(s1 is s2)
# Exanple 3 returns true since Sony and Sony are same


# An alias relationship is said to exist between references of objects if they refer to the same object allocated in memory during execution. A set is a pair of references that satisfy alias relationships between objects.

a1 = [40, 50, 60, 70]

a2 = [20, 30, 40, 50]
# alias


a2 = a1

a2.append("4000")
a1.append("100")

print(a1)


# A function that accepts list as argument and returns an out put modified list.
def modify_list(ls):
    a = ls
    b = a




