import random

# DETERMINE PASSWORD LENGTH
def PasswordLength():

    while True:
        PasswordLength = input("How long would you like your password to be?\n8 characters\n12 characters\n16 characters\nPlease type in your answer:")
        if PasswordLength == "8" or PasswordLength == "12" or PasswordLength == "16":
            print(" ")
            break
        print('ERROR: Please only type in either "8", "12", or "16"\n')

    PasswordLength = int(PasswordLength)
    return PasswordLength

# SET PASSWORD PREFERENCES
def PasswordPreferences():

    Length = PasswordLength()

    while True:
        RandomizeOption = input("Would you like to add preferences to your password?\nYES or NO\nPlease type in your answer: ")
        if RandomizeOption.upper() == "YES" or RandomizeOption.upper() == "NO":
            print(" ")
            break

    if RandomizeOption.upper() == "NO":

        Random_LowercaseLetterQuantity = random.randint(0, Length)
                
        NewLength = Length - Random_LowercaseLetterQuantity
        Random_UppercaseLetterQuantity = random.randint(0, NewLength)

        NewLength = NewLength - Random_UppercaseLetterQuantity
        Random_DigitQuantity = random.randint(0, NewLength)

        NewLength = NewLength - Random_DigitQuantity
        Random_SpecialCharacterQuantity = random.randint(0, NewLength)

        Password = GeneratePassword(Random_LowercaseLetterQuantity, Random_UppercaseLetterQuantity, Random_DigitQuantity, Random_SpecialCharacterQuantity, Length)
        print(f"Your randomly generated password is: {Password}\n")

        ExportPassword(Password)
        AskGenerateAgain()

    else:
        while True:
            LowercaseQuantity = input("How many lowercase letters do you want to have? ")
            try:
                LowercaseQuantity = int(LowercaseQuantity)
                if LowercaseQuantity >= 0 and LowercaseQuantity <= Length:
                    print(" ")
                    break
                print(f"ERROR: Please enter a number between 0 and {Length}\n")
            except:
                print("ERROR: Please type in a number\n")

        NewLength = Length - LowercaseQuantity

        while True:
            UppercaseQuantity = input("How many uppercase letters do you want to have? ")
            try:
                UppercaseQuantity = int(UppercaseQuantity)
                if UppercaseQuantity >= 0 and UppercaseQuantity <= NewLength:
                    print(" ")
                    break
                print(f"ERROR: Please enter a number between 0 and {NewLength}\n")
            except:
                print("ERROR: Please type in a number\n")

        NewLength = NewLength - UppercaseQuantity
        
        while True:
            DigitQuantity = input("How many digits do you want to have? ")
            try:
                DigitQuantity = int(DigitQuantity)
                if DigitQuantity >= 0 and DigitQuantity <= NewLength:
                    print(" ")
                    break
                print(f"ERROR: Please enter a number between 0 and {NewLength}\n")
            except:
                print("ERROR: Please type in a number\n")

        SpecialCharacterQuantity = NewLength - DigitQuantity

        #print(LowercaseQuantity)
        #print(UppercaseQuantity)
        #print(DigitQuantity)
        #print(SpecialCharacterQuantity)
                
        Password = GeneratePassword(LowercaseQuantity, UppercaseQuantity, DigitQuantity, SpecialCharacterQuantity, Length)
        print(f"Your randomly generated password is: {Password}\n")

        ExportPassword(Password)
        AskGenerateAgain()

def ExportPassword(P_Password):
    Password = P_Password

    Filename = input("Save the file as: ")
    Filename += ".txt"

    with open(Filename, 'w') as PasswordFile:
        PasswordFile.write(Password)
        PasswordFile.close()

# GENERATE RANDOM PASSWORD
def GeneratePassword(P_LowercaseLetterQuantity, P_uppercaseLetterQuantity, P_DigitQuantity, P_SpecialCharacterQuantity, P_PasswordLength):
    Password = ""
    
    for i in range(P_LowercaseLetterQuantity):
        RandomIndex = random.randint(0, len(LOWERCASE_LETTERS)-1)
        Password += LOWERCASE_LETTERS[RandomIndex]

    for i in range(P_uppercaseLetterQuantity):
        RandomIndex = random.randint(0, len(UPPERCASE_LETTERS)-1)
        Password += UPPERCASE_LETTERS[RandomIndex]

    for i in range(P_DigitQuantity):
        RandomIndex = random.randint(0, len(DIGITS)-1)
        Password += DIGITS[RandomIndex]

    for i in range(P_SpecialCharacterQuantity):
        RandomIndex = random.randint(0, len(SPECIAL_CHARACTERS)-1)
        Password += SPECIAL_CHARACTERS[RandomIndex]
        
    return Password

# ASK IF THE USER WANTS TO GENERATE A NEW RANDOM PASSWORD
def AskGenerateAgain():
    while True:
        Continue = input("Would you like to generate another password?\nYES or NO\nPlease type in your answer: ")
        print(" ")
        if Continue.upper() == "YES" or Continue.upper() == "NO":
            break

    if Continue.upper() == "YES":
        print(" ")
        PasswordPreferences()
    else:
        exit("You have successfully exited the program")

#############################################################

LOWERCASE_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPERCASE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL_CHARACTERS = ["!", "?", ".", "_", "-", "$", "#"]

PasswordPreferences()

    
