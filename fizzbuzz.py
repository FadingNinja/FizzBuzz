num = 1
while num <= 100 :
    if num % 3 == 0 and num % 5 == 0 :
        print(f"{num} = FizzBuzz")
    elif num % 3 == 0 :
        print(f"{num} = Fizz")
    elif num % 5 == 0 :
        print(f"{num} = Buzz")
    else :
        print(num)
    num = num + 1
