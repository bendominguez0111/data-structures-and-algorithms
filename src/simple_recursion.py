# given a positive integer n, print the sum of all the positive integers leading up to n

def simple_recursion(n):

    print(n) #pre

    #base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    sum_n = n + simple_recursion(n-1) #recursion
    
    print(n, sum_n) # post => this is where we start climbing out of the stack

    return sum_n

if __name__ == '__main__':
    print(
       simple_recursion(5)
    )