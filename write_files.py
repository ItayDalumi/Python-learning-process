# with open("wrote_by_python.txt",'w') as file:
#     file.write("this is very cool")

# this is makes a new file and then we can add some text to it.
# if we already create the file and we add text and run the program again this will just append the new text to the file.

# its better in this case to use the append option:

# with open("wrote_by_python.txt", 'a') as file:
#     file.write("\nthis is a new line!")

# but every time this program will run the "this is a new line!" will add to this file because we use append and not write.

with open("emails.txt", 'r') as emails:
    emails = emails.readlines() # this will save all the emails.txt text in the variable "emails"

for email in emails:
    if "4" in email:
        print(email.rstrip()) # the rstrip() is the python way to do "trim" so it will remove all the blank lines