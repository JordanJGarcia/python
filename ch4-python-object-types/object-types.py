#! /usr/bin/python3

"""
Python programs can be decomposed into modules, statements,
expressions, and objects, as follows:

    1. Programs are composed of modules
    2. Modules contain statements
    3. Statements contain expressions
    4. Expressions create and process objects
"""

"""
Here is a list of Python's built-in object types:

    Numbers (immutable)
    Strings (immutable)
    Lists
    Dictionaries
    Tuples  (immutable)
    Files
    Sets
    Other core types (Booleans, types, None)
    Program unit types (Functions, modules, classes)
    Implementation-related types (Compiled code, stack tracebacks)
"""



"""
    STRINGS
"""
S = 'Spam'
print("S:", S);
print("S.find('pa'):", S.find('pa'))

# remember that strings are immutable
# so this actually returns a new string object
# with the replaced characters
print("S.replace('pa', 'XYZ'):", S.replace('pa', 'XYZ'))

# to demonstrate 'S' wasn't modified
print("S:", S)

# upper case conversion
print("S.upper():", S.upper())

# split on a delimiter into a list of substrings
line = 'aaa,bbb,ccccc,dd'
print("line:", line)
print("line.split(','):", line.split(','))

# remove whitespace characters on right side
line = 'aaa,bbb,ccccc,dd\n'
print("line (theres a newline at the end):", line)
print("line.rstrip():", line.rstrip())
print("line.rstrip().split(','):", line.rstrip().split(','))
print("line.split(','):", line.split(','))

# formatting expression
print('%s, eggs, and %s' %('spam', 'SPAM!'))

# formatting method (2.6+, 3.0+)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))

# numbers optional (2.7+, 3.1+)
print('{}, eggs, and {}'.format('spam', 'SPAM!'))

# more formatting examples
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

# As a rule of thumb:
# generic operations that span multiple types show up as built-in functions or expressions (len(x) or x[0])
# type-specific operations are method calls (string.upper())


print('\nFor more details, we can always call the built-in "dir" function')
print('This function lists variables assigned in the caller\'s scope when called with no argument')
print('But more usefully, it returns a list of all the attributes available for any object passed to it')
print('Methods are function attributes, so they will show up in the list:')
print('\ndir(S):', dir(S))

print('\nThe "dir" function simply gives the methods\' names.')
print('To ask what they do, you can pass them to the "help" function:')
print("help(S.replace) - ** run this in interactive mode so it displays properly **")
