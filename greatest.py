# Find the greatest among two numbers

def findGreatest (FirstNumber, SecondNumber):
    if FirstNumber > SecondNumber:
        print("first number is greater")
    elif SecondNumber > FirstNumber:
        print("second number is greater")
    else:
        print("tne number are equal")


FirstNumber =int(input("enter the first numbers : "))
SecondNumber =int(input("enter the second numbers : "))
findGreatest(FirstNumber, SecondNumber)
