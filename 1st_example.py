# This is an example for a scipt with no libraries or GUI for testing purposes
# Try pyinstaller on this example

def main():
    answer = input("Y/N: ")
    a = answer.upper()

    if a == 'Y':
        print("Your input was Y")

    elif a == 'N':
        print("Your input was N")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
