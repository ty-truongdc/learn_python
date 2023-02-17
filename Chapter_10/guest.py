#Write a program that prompts the user for their name. When they respond,
#  write their name to a file called guest.txt

while True:
    filename = "guest_book.txt"
    name = input("What is your name?")
    with open(filename,'a') as file_object:
        file_object.write(name)
    if name == 'q':
        break