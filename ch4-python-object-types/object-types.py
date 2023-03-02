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

print("Read this file for more information");

# As a rule of thumb:
# generic operations that span multiple types show up as built-in functions or expressions (len(x) or x[0])
# type-specific operations are method calls (string.upper())


print('\nFor more details, we can always call the built-in "dir" function')
print('This function lists variables assigned in the caller\'s scope when called with no argument')
print('But more usefully, it returns a list of all the attributes available for any object passed to it')
print('Methods are function attributes, so they will show up in the list:')

print('\nThe "dir" function simply gives the methods\' names.')
print('To ask what they do, you can pass them to the "help" function:')
print("help(S.replace) - ** run this in interactive mode so it displays properly **")

print("\nOne nice feature of Python's core data types is that they support arbitrary nesting")
print("We can nest them in any combination, and as deeply as we like")
