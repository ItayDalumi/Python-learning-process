file_name = input("file name: ")
if ".txt" not in file_name:
    file_name = file_name + ".txt" #makes it a txt file

content = input("write the file content: ")

with open(file_name, 'w') as file:
    file.write(content)

if input("do you want to read the file? (yes/no)") == "yes":
    with open(file_name, 'r') as file:
        print(file.read())