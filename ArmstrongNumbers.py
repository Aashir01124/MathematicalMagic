a = 1
while a>0:
    number = int(input("Enter the number: "))
    digits = len(str(number))
    resNum = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        resNum += digit ** digits
        temp //= 10
    
    if number == resNum:
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")