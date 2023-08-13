def main():
    def fibo(n : int):
        if n == 0: return 0
        elif n == 1: return 1

        return fibo(n-1) + fibo(n-2)

    n = int(input("n = "))
    print(fibo(n))

if __name__ == '__main__':
    main()