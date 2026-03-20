# Program to find Armstrong numbers from 10 entered numbers

print("Enter 10 numbers:")
for i in range(10):
    num = int(input("Enter number: "))
    temp = num
    sum = 0
    digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    if sum == num:
        print(num, "is an Armstrong number")
