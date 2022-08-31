'''
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

note: Redesigned this problem solution to use the readlines method, and be universal in the assumption that all lines,
except the last line, will contain a \n at the end (not to be included in character count).

Problem source: SoloLearn
Problem objective: Read files
'''
file = open("Book_titles/books.txt", "r")

#your code goes here
# Q: What do I want to do?
# Answer:
# 1. index through a list with the book titles
# 2. skip the odd elements in the list
# 3. count the characters in each title, except the \n
# 4. skip the final element in terms of omitting \n
# 5. print the first character of each title with the character count next to it, in a loop

# assign the file contents to a list named "read"
read = file.readlines()
# 
n = len(read) - 1
i = 0
print(read)
while i < n:
    if(i%2 == 0):
        print(read[0:n])
        i+=1
    else:
        i+=1
        continue

file.close()