#! /usr/bin/python3

print("The tuple object is roughly like a list that you cannot change")
print("Hence it is immutable, and it is a sequence")

print("\nFunctionally, they are used to represent fixed collections of items")
print("Syntactically, they are normally coded in parentheses instead of square brackets, and they support arbitrary")
print("types, arbitrary nesting, and the usual sequence operations")

print("\ndir(tuple):\n")
print(dir(tuple))

T = (1, 2, 3, 4)
print("\nT:", T)

print("\nlen(T):", len(T))

print("\nT + (5, 6):", T + (5, 6))
print("\nT[0]:", T[0])

print("\nTuples also have type-specific callable methods, but not as many as lists:")
print("\nT.index(4):", T.index(4))
print("\nT.count(4) # how many times does '4' appear:", T.count(4))

print("\nOne-item tuples require a trailing commma:")
print("\nT = (2,)")
T = (2,)
print("T:", T)
print("type(T):", type(T))

print("\nT = (2)")
T = (2)
print("T:", T)
print("type(T):", type(T))
