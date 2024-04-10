# This is my first GitHub addition

def encode_password(choice):
    temp = [int(i) for i in choice]
    temp2 = [str(i+3) for i in temp]
    choice = "".join(temp2)

    return choice

def decode(choice):
    pass
    # Here is my decode function!


def main():
    while True:
        encode = 0
        original = 0
        print("Menu")
        print("-------------")
        print("1 Encode")
        print("2. Decode")
        print("3. Quit")
        user = int(input("Please enter an option: "))
        if user == 1:
            input1 = input("Please enter your password to encode: ")
            encode = encode_password(input1)
            original = input1
            print("Your password has been encode and stored!")
        elif user == 2:
            print(f"The encoded password is {encode}, and the original password is {original})")
        elif user == 3:
            break

main()
