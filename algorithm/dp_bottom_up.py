def Fibonacci(N):
    Fib = [None] * (N+1)
    Fib[0] = 0
    Fib[1] = 1
    for i in range(2, N+1):
        Fib[i] = Fib[i-1] + Fib[i-2]
    return Fib[N]


if __name__ == "__main__":
    n = int(input())

    if n<=1:
        print(n)
    else:
        print(Fibonacci(n))