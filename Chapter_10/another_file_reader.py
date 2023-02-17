#Read and print the whole file using read method
filename = 'learning_python.txt'
with open (filename) as file_object:
    content = file_object.read()
    print(content.strip())
#print out file line by line using loop
with open (filename) as file_object:
    for line in file_object:
       print(line.strip())
#print out file using readlines method, then save it to a variable to use it outside of 'with' block
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip()) 

#Replace the word Python with C if found in text file:

if "Python" in line:
    line.replace('Python', 'C')
    print(line.strip())