#This is way to search within a file
def search(f):
    for line in f:
        if line.startswith("Hello"):
            print(line)

def countLines(f):
    count = 0
    for line in f:
        print(line)
        count = count + 1
    print("This document has",count, "lines")          

f = open("Python for everybody - freecodecamp/read a file/example.txt")

search(f)
countLines(f)

"""
If I try to use f.read and then I try to count the number of lines whithin the file,
it returns 0, right now idk what is the reason, but another thing that I realized is that 
if I use a for loop to print the file's content, it display an empty line after each linea 
whit content, it happend since each file's line ends with \n and print put one more \n
"""

"""
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
"""

