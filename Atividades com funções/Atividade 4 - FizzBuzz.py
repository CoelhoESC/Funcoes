def FizzBuzz(N1=0):
    if N1 % 3 == 0 and N1 % 5 == 0:
        return 'FizzBuzz'
    elif N1 % 5 == 0:
        return 'Buzz'
    elif N1 % 3 == 0:
        return 'Fizz'
    else:
        return N1


print(FizzBuzz(500))
