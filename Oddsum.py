#sum the Odd number
sum = 0
for number in range(1,11):
    if number % 2 != 0:
        sum = sum + number
        print(sum)
