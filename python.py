def fibs_fizz_buzz(n):
    fib_seq = [1]
    if n > 1:
        fib_seq.append(1)
        
    while len (fib_seq) < n :
        next_number = fib_seq [-1] + fib_seq [-2]
        fib_seq.append(next_number)
    
    result = []
    
    for num in fib_seq:
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(num)

    return result
