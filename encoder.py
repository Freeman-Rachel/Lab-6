#Rachel Freeman
def encoder(encodee):
    encoded = ""
    for n in encodee:
        n = str(int(n)+3) #encodes the password
        encoded += n
    return encoded

def password_decoder(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_password += str(int(digit) - 3) #return the password
    return decoded_password


select = 0
menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit" #menu

while True: #while loop in order to run the menu multiple times
    while select != 3:
        print(menu) #prints the menu
        select = int(input("Please enter an option: ")) #takes user input
        if select == 1:
            encodee = input("Please enter your password to encode: ") #takes in encodee input to put in function
            print("Your password has been encoded and stored!")
            encoded = encoder(encodee) #puts in encoder function
        if select == 2:
            correct_password = password_decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {correct_password}.")

    if select == 3:
        break #breaks from the loop
#The second part decode is done my Andrew Griner