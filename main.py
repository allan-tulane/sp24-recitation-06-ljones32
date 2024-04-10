def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n < 2:
        return n
    else:
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    if fibs[n] != -1:
      return fibs[n]
    if n < 2:
      return n
    else:
      fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
      return fibs[n]


def fib_bottom_up(n):
    fibs = [0] * (n+1)
    for i in range(n+1):
        if i < 2:
            fibs[i] = i
        else:
            fibs[i] = fibs[i-1] + fibs[i-2]
    print(fibs)
    return fibs[-1]




