# Encoder program by Sherif Abdou
def encode(password):
    result = ""
    for digit in password:
        result += f"{(int(digit) + 3)%10}"
    return result


def print_menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


if __name__ == "__main__":
    encoded_password = ""
    while True: # Simple user loop
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter a password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if choice == 3:
            exit()

