# Write a program to check palindrome.

def main():
    string = input("Enter a value:\n")
    palindrome(string)

def palindrome(string):
    rev_string = string[::-1]
    if string == rev_string:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

if __name__ == "__main__":
        main()


