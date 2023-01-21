from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length = 8,
    uppercase = 2,
    numbers = 2,
    special = 2,
    nonletters = 2,
)

password_xmpl = "password123456"

title = input("What do you want the file to be titled?")

file_name = title + ".txt"

with open(file_name, 'w') as password_file:
    password_file.write(password_xmpl)
    password_file.close()

