a = 1
while a:
    def Factors(number):
        print("The factors of ",number,"are: ")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)
            
    number = int(input("Enter your number to find the factors: "))
    Factors(number)