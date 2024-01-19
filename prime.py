# Write a program to find prime number with in a range using function.

def main():
    number = int(input('Enter any number:\n'))
    prime(number)
    
def prime(num):
    count = 0
    for i in range (1, num+1):
        if num%i == 0:
            count+= 1
    if count == 2 :
        print(' It is a Prime Number')
    else:
        print(' It is not a Prime Number')
       
if __name__ == "__main__":
        main()