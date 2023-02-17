"""Write a while loop that prompts users for their name. When
they enter their nam, print a greeting to the screen and add 
a line recording their visit in a file called guest_book.txt.
Make sure each entry appears on a new line in the file."""

print("Welcome to our business.")
#filename = "guest_book2.txt"
name = input("Please enter your name.\n Enter q if you want to quit.\n")
while name != 'q':
    
    with open("guest_book.txt", 'a') as file_object:
        file_object.write(f"{name.title()}\n")
        name = input("Please enter your name.\n Enter q if you want to quit.\n")
    
