# Read input as specified in the question.
def fib(n1):
    a = 1
    b = 1
    i = 2
    if n1 < 0:
        print("wrong input")
    elif n1 == 0:
        return a
    elif n1 == 1:
        return b
    else:
        while i < n1:
            c = a + b
            a = b
            b = c
            i += 1
        return c


n = int(input())
# Print output as specified in the question.
print(fib(n))