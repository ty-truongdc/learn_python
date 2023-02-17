"""Write a while loop that asks people why they like 
programming.  Each time someone enters a reason, add their reason to a file that stors all the responses"""

response = input("Please enter your reason why you like programming.\nEnter q to quit.")
while response != 'q':
    with open("people_like_programming.txt", 'a')  as file_object:
        file_object.write(f"{response.capitalize()}\n")
        response = input("Please enter your reason why you like programming.")
