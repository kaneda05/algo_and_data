def main():

    k = int(input('number : '))
    memo = [-1] * (k + 1)
    memo[0] = 0
    memo[1] = 1

    def fibo(n : int):
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = fibo(n-1) + fibo(n-2)

        return memo[n]

    fibo(k)
    print('result : {}'.format(memo[-1]))

if __name__ == '__main__':
    main()