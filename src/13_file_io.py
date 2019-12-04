"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('C:/Users/Owner/Desktop/lambda/CS24/w1-Intro-To-Python-and-OOP/Intro-Python-I/src/foo.txt') as f: 
    read_data = f.read()
    print(read_data)
    f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

w= open('bar.txt', 'w')
w.write("Is the arbitrary content? /n Is this arbitrary content? /n Of course.")
w.close()