#! /usr/bin/python3

print("File objects are Python code’s main interface to external files on your computer")
print("\nFiles are a core type, but they’re something of an oddball")
print("There is no specific literal syntax for creating them. Rather, to create a file object,")
print("you call the built-in open function, passing in an external filename and an optional processing mode as strings");

print("\n# f = open('data.txt', 'w')")
f = open("data.txt", "w")
print("\ndir(f):\n\n", dir(f))

print("\nRead the code to see how to open and write to a file...")
numWritten = f.write("hello\n") # returns number of characters written
print("data.txt: wrote (%1d) bytes" % (numWritten))

numWritten = f.write("world")
print("data.txt: wrote (%1d) bytes" % (numWritten))

f.close()

print("\nRead the code to see how to open and read from a file...")
f = open("data.txt") # defaults to "r" mode
text = f.read()
print("text in data.txt:\n'%s'" % (text))
print("text.split():", text.split())

f.close()

print("\nA one-liner for your entertainment:")
print("\nfor line in open('data.txt'): print(line)")
for line in open('data.txt'): print(line)

print("\nbinary files are useful for processing media, accessing data created by C programs")
print("and so on. Python's struct module can both create and unpack packed binary data - raw")
print("bytes that record values that are not Python objects - to be written ot a file in binary mode")

import struct

# create a packed binary data 10 bytes, 
# not objects or text
print("\n# create a packed binary data 10 bytes,")
print("# not objects or text")
print("# see help(struct) for more info")
print("# think of the below format string as:")
print("# > - big endian, i - int (4 bytes), 4s - 4 char string, h - short (2 bytes)")
print("packed = struct.pack('>i4sh', 7, b'spam', 8)")
packed = struct.pack('>i4sh', 7, b'spam', 8)
print("packed:", packed)
print("Now writing it to 'data.bin'")
file = open('data.bin', 'wb')
file.write(packed)
file.close()

print("\nNow reading from file 'data.bin'")
print("# data = open('data.bin', 'rb').read()")
data = open('data.bin', 'rb').read()
print("data:", data)
print("data[:4]:", data[:4])
print("data[4:8]:", data[4:8])
print("data[8:]:", data[8:])
print("list(data):", list(data))
print("struct.unpack('>i4sh', data):", struct.unpack('>i4sh', data))

