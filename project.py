# file = open("filename", "mode")
# Mode Description
#------------------------------
# 'r' Read (default mode)
# 'w' Write (overwrites if exists)
# 'a' Append (adds to end of file)
# 'r+' Read and write
# Write
file = open("hello.txt", "w")
file.write("Hello, World!\n")
file.write("This is a new file.\n")
file.close()
# Best Practice
# use the with statement which auto-closes the file
with open("hello.txt", "w") as file:
 file.write("Safe file handling with 'with'.")
# To Read entire content
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()
# To read line by line
with open('hello.txt','r'):
 for line in file:
  print(line.strip)
# Append
file = open("hello.txt", "a")
file.write("This line is added.\n")
file.close()
# To close the file
# close(