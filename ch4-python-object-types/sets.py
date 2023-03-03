#! /usr/bin/python3

print("Sets are neither mappings nor sequences")
print("They are unordered collections of unique and immutable objects")
print("They support the usual set operations")

print("\ndir(set):\n")
print(dir(set))

print("\n# X = set('spam')")
X = set('spam')
print("# Y = {'h', 'a', 'm'}")
Y = {'h', 'a', 'm'}

print("\nX:", X)
print("Y:", Y)
print("\n(Intersection) X & Y:", X & Y)
print("(Union)        X | Y:", X | Y)
print("(Difference)   X - Y:", X - Y)
print("(Difference)   Y - X:", Y - X)
print("(Superset)     X > Y:", X > Y)

print("\nSet comprehensions:")
print("\n# {n ** 2 for n in [1, 2, 3, 4]}")
print({n ** 2 for n in [1, 2, 3, 4]})

print("\nSets can be useful for common tasks such as:")
print("\tfiltering out duplicates")
print("\tisolating differences")
print("\tand performing order-neutral equality tests without sorting")
print("in lists, strings, and other iterable objects")

print("\n# filtering out duplicates:")
print("# list(set([1, 2, 1, 3, 1]))")
print(list(set([1, 2, 1, 3, 1])))

print("\n# finding differences in collections:")
print("# set('spam') - set('ham')")
print(set('spam') - set('ham'))

print("\n# order-neutral equaliting tests (== is False)")
print("# set('spam') == set('asmp')")
print(set('spam') == set('asmp'))
