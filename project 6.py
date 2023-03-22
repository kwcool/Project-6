   # encode by kyle weiner
   # decode added by jaden despeines

def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(encoded_password):
    original_pw = ""
    for char in encoded_password:
        if int(char) < 3:
            original_pw = original_pw + str(int(char) + 7)
        else:
            original_pw = original_pw + str(int(char) - 3)
    return original_pw


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        elif choice == '3':
            break
        else:
            print("Invalid")
