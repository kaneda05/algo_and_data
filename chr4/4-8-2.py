def main():

    from functools import lru_cache

    @lru_cache
    def fibo(n: int):
        if n == 0: return 0
        if n == 1: return 1

        result = fibo(n-1) + fibo(n-2)

        return result

    n = int(input('number : '))
    print("result : {}".format(fibo(n)))

if __name__ == '__main__':
    main()