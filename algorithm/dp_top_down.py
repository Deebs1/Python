result = [-1] * 100

def Fibonacci(N):
    if result[N] == -1:
        if N<=1:
            result[N] = N
        else:
            result[N] = Fibonacci(N-1) + Fibonacci(N-2)

    return result[N]

if __name__ == "__main__":
    n = int(input())

    if n<=1:
        print(n)
    else:
        print(Fibonacci(n))