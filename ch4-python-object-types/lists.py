#! /usr/bin/python3

print("Lists are positionally ordered collections of arbitrarily typed objects")
print("and they have no fixed size")
print("and they are mutable")

print("\ndir(list):")
print(dir(list))

print("\nHere are some type specific operations:")
L = [123, 'spam', 1.23]
print("L:", L)
print("L.append('NI')...")
L.append('NI')
print("L:", L)
print("L.pop(2):", L.pop(2))
print("L:", L)

M = ['bb', 'aa', 'cc']
print("\nM:", M)
print("M.sort()...")
M.sort()
print("M:", M)
print("M.reverse()...")
M.reverse()
print("M:", M)

print("\nNested list:")
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(M)
print("M[1]:", M[1])
print("M[1][2]:", M[1][2])
