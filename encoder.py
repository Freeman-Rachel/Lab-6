def encoder(encodee):
    encoded = ""
    for n in encodee:
        n = str(int(n)+3)
        encoded += n
    return encoded



select = 0
menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"

while True:
    while select != 3:
        print(menu)
        select = int(input("Please enter an option: "))
        if select == 1:
            encodee = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        if select == 2:
            print(f"The encoded password is {encoder(encodee)}, and the original password is {encodee}.")
    if select == 3:
        exit
