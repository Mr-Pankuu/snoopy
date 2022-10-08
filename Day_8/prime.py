def prime(a):
    if a % 2 == 0 or a % 3 == 0 or a% 5 == 0 or a % 7== 0:
        print("It is not prime number")
    else:
        print("Its prime number")

n = int(input("Enter the number to check the prime number : "))
prime(a=n)