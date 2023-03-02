#! /usr/bin/python3

print("Lists are positionally ordered collections of arbitrarily typed objects")
print("and they have no fixed size")
print("and they are mutable")

print("\ndir(list):")
print(dir(list))

print("\nHere are some type specific operations:")
L = [123, 'spam', 1.23]
print("L:", L)
print("\n# L.append('NI')")
L.append('NI')
print("L:", L)
print("\n# L.pop(2):")
L.pop(2)
print("L:", L)

M = ['bb', 'aa', 'cc']
print("\nM:", M)
print("\n# M.sort()")
M.sort()
print("M:", M)
print("\n# M.reverse()")
M.reverse()
print("M:", M)

print("\nNested list:")
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(M)
print("M[1]:", M[1])
print("M[1][2]:", M[1][2])

print("\nIn addition to sequence operations and list methods, Python includes a more")
print("advanced operation known as a list comprehension expression, which turns out")
print("to be a powerful method to process structures like our matrix")

print("\nList comprehensions derive from set notation; they are a way to build a new list by")
print("running an expression on each item in a sequence, one at a time, from left to right")
print("They are composed of an expression and a looping construct that share a variable name (in this case: 'row')")

M = [[1,2,3], [4,5,6], [7,8,9]]
print("\nM:", M)

col2 = [row[1] for row in M]
print("\n# row[1] for each row in matrix M")
print("[row[1] for row in M]:", col2)

print("\nMore complex list comprehensions:\n")
lc1 = [row[1] + 1 for row in M] # add 1 to each item in col 2
print("# add 1 to each item in col 2")
print("[row[1] + 1 for row in M]:", lc1)

lc2 = [row[1] for row in M if row[1] % 2 == 0] # filter out odd items
print("\n# filter out odd items")
print("[row[1] for row in M if row[1] % 2 == 0]:", lc2)

diag = [M[i][i] for i in [0, 1, 2]]
print("\n# collect a diagonal from matrix")
print("[M[i][i] for i in [0, 1, 2]]:", diag)

doubles = [c * 2 for c in 'spam']
print("\n# repeat characters in a string")
print("[c * 2 for c in 'spam']:", doubles)

print("\nThe following illustrates using range() - a built-in that generates")
print("successive integers, and requires a surrounding list to display all its values")

print("\n# list(range(4))")
print(list(range(4)))

print("\n# list(range(-6, 7, 2))")
print(list(range(-6, 7, 2)))

print("\n# [[x ** 2, x ** 3] for x in range(4)]")
print([[x ** 2, x ** 3] for x in range(4)])

print("\n# [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]")
print([[x, int(x / 2), x * 2] for x in range(-6, 7, 2) if x > 0])

print("\nYou'll find that in recent Pythons, comprehension syntax has been generalized for other roles:")
print("its not just form making lists today")
print("For example, enclosing a comprehension in parentheses can also be used to create generators that")
print("produce results on demand:")

print("\nM:", M)
print("\n# G = (sum(row) for row in M)")
G = (sum(row) for row in M)
print("\n# next(G) (3 times)")
print(next(G))
print(next(G))
print(next(G))


print("\nIn Python 3.X, comprehension sytnax can also be used to create sets and dictionaries:")
print("\n# {sum(row) for row in M} - set")
s = {sum(row) for row in M}
print(s)

print("\n# {i : sum(M[i]) for i in range(3)} - dict")
d = {i : sum(M[i]) for i in range(3)}
print(d)
