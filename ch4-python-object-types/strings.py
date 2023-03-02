#! /usr/bin/python3

"""
    STRINGS
"""

print("Strings are used to record both textual information as well as arbitrary collections of bytes")
print("They are sequences - a positionally ordered collection of other objects")
print("Sequences maintain a left-to-right order among the items they contain, and their items")
print("are fetched by their relative position")
print("They are also immutable")

print('\ndir(str):\n', dir(str))

S = 'Spam'
print("\nS:", S);
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

# other ways to code strings
S = 'A\nB\tC'
print("S:", S)
print("len(S):", len(S))
print("ord('\\n'):", ord('\n'))

S = 'A\0B\0C'
print("S:", S)
print("len(S):", len(S))


# multiline string
msg = """
aaaaaaaaaaaaaaaaaa
bbb'''bbbbbbbbbbbb""bbbbbbbbb'bbbb
cccccccccccccccccc
"""
print(msg)


# raw string literal
# this turns off the backslash escape mechanism
raw = r'C:\text\new'
print(raw)

# unicode strings
uni = u'sp\xc4m'
print(uni)
