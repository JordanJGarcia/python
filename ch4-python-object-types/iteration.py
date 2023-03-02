#! /usr/bin/python3

print("In a nutshell, an object is iterable if it is either:")
print("\tA physically stored sequence in memory, or")
print("\tAn object that generates one item at a time in the context of an iteration operation - a sort of 'virtual' sequence")

print("\nBoth these types of objects are iterable because they support the iteration protocol")
print("\nAn example of the latter type of object is the 'generator comprehension' in the 'lists.py' file")
print("Its values aren't store in memory all at once, but are produced as requested, usually by iteration tools")
print("Another example is a python file object, which iterates line by line when used by an iteration tool")
print("file content is fetched on demand")
