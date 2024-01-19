# Write a program to generate the Fibonacci sequence of a given number.

def main():
    number =  int (input('enter a value:\n'))
    fibonnaci(number)

def fibonnaci(number):
    first_value = 0
    second_value = 1
    for i in range (0,number):
        current_value = first_value
        print(current_value)
        print("\n")
        first_value = second_value
        second_value = current_value + first_value

if __name__ == "__main__":
        main()


