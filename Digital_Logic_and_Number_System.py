def binary_to_decimal():
    b = input("Enter integer binary number: ")
    print("Decimal:", int(b, 2))


def decimal_to_binary():
    d = int(input("Enter integer decimal number: "))
    print("Binary:", bin(d)[2:])


def binary_to_octal():
    b = input("Enter integer binary number: ")
    print("Octal:", oct(int(b, 2))[2:])


def octal_to_binary():
    o = input("Enter integer octal number: ")
    print("Binary:", bin(int(o, 8))[2:])


def hex_to_decimal():
    h = input("Enter integer hexadecimal number: ")
    print("Decimal:", int(h, 16))


def decimal_to_hexadecimal():
    d = int(input("Enter integer decimal number: "))
    print("Hexadecimal:", hex(d)[2:].upper())


def and_gate():
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print("AND Output:", a & b)


def or_gate():
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print("OR Output:", a | b)


def xor_gate():
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print("XOR Output:", a ^ b)


def binary_to_gray():
    b = input("Enter integer binary number: ")

    # validate input
    for ch in b:
        if ch not in "01":
            print("Invalid binary number!")
            return

    gray = b[0]  # MSB remains same

    for i in range(1, len(b)):
        gray += str(int(b[i - 1]) ^ int(b[i]))

    print("Gray Code:", gray)


def ninth_complement():
    n = input("Enter integer number: ")
    result = "".join(str(9 - int(d)) for d in n)
    print("9's Complement:", result)


def tenth_complement():
    n = input("Enter integer number: ")
    nine_comp = "".join(str(9 - int(d)) for d in n)
    ten_comp = str(int(nine_comp) + 1)
    print("10's Complement:", ten_comp)


# -------- MAIN MENU --------
while True:
    print("\n===== DIGITAL & NUMBER SYSTEM MENU =====")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Binary to Octal")
    print("4. Octal to Binary")
    print("5. Hexadecimal to Decimal")
    print("6. Decimal to Hexadecimal")
    print("7. AND Gate")
    print("8. OR Gate")
    print("9. XOR Gate")
    print("10. Binary to Gray Code")
    print("11. 9's Complement")
    print("12. 10's Complement")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        binary_to_decimal()
    elif choice == "2":
        decimal_to_binary()
    elif choice == "3":
        binary_to_octal()
    elif choice == "4":
        octal_to_binary()
    elif choice == "5":
        hex_to_decimal()
    elif choice == "6":
        decimal_to_hexadecimal()
    elif choice == "7":
        and_gate()
    elif choice == "8":
        or_gate()
    elif choice == "9":
        xor_gate()
    elif choice == "10":
        binary_to_gray()
    elif choice == "11":
        ninth_complement()
    elif choice == "12":
        tenth_complement()
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
