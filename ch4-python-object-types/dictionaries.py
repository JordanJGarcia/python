#! /usr/bin/python3

print("Python dictionaries are something completely different")
print("They are not sequences, but are instead known as mappings")
print("\nMappings are also collections of other objects, but they store")
print("objects by key instead of by relative position")
print("They are also mutable. Like lists, they may be changed in place and can")
print("grow and shrink on demand\n")

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print("D:", D)

print("\n# D['food']")
print(D['food'])

print("\n# D['quantity'] += 1")
D['quantity'] += 1
print(D)

print("\n# D = {}")
D = {}
print("# D['name'] = 'Bob'")
D['name'] = 'Bob'
print("# D['job'] = 'dev'")
D['job'] = 'dev'
print("# D['age'] = 40")
D['age'] = 40

print("\nD:", D)

print("\nAlternative ways to make dictionaries:")
print("\n# bob1 = dict(name='Bob', job='dev', age=40)")
bob1 = dict(name='Bob', job='dev', age=40)
print("bob1:", bob1)
print("\n# bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))")
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print("bob2:", bob2)

print("\nNesting revisited:")
s = """ rec = {'name': {'first': 'Bob', 'last': 'Smith'},
               'jobs': ['dev', 'mgr'],
               'age': 40.5} """
print("\n#", s)
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
      'jobs': ['dev', 'mgr'],
      'age': 40.5}

print("\n# rec['name']")
print(rec['name'])
print("\n# rec['name']['last']")
print(rec['name']['last'])
print("\n# rec['jobs']")
print(rec['jobs'])
print("\n# rec['jobs'][-1]")
print(rec['jobs'][-1])
print("\n# rec['jobs'].append('janitor')")
rec['jobs'].append('janitor')
print(rec['jobs'])
print("\nrec:", rec)


print("\nThe dictionary 'in' membership expression allows us to query the existence")
print("of a key and branch on the result with a python if statement")
D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99
print("D:", D)
print("\n# 'f' in D")
res = 'f' in D
print(res)

print("\nif not 'f' in D:")
print("\tprint('missing')")
if not 'f' in D:
    print('missing')


print("\nOther ways to test for key existence:")
print("\n# value = D.get('x', 0) - remember you can use help(dict.get) for more info...")
value = D.get('x', 0)
print(value)

print("\nvalue = D['x'] if 'x' in D else 0")
value = D['x'] if 'x' in D else 0
print(value)

print("\nSorting dictionaries:")
print("Because dictionaries are not sequences, they do not maintian any dependable left-to-right order.")

print("\n# Ks = list(D.keys())")
Ks = list(D.keys())
print("Ks:", Ks)
print("\n# Ks.sort()")
Ks.sort()
print("Ks:", Ks)

print("\n# for key in Ks:")
print("#     print(key, '=>', D[key])")
for key in Ks:
    print(key, '=>', D[key])

print("\nYou can do it in one step instead of three:\n")
print("D:", D)
print("\n# for key in sorted(D):")
print("#     print(key, '=>', D[key])")
for key in sorted(D):
    print(key, '=>', D[key])
