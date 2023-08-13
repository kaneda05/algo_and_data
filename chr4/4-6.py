def main():

    def fibo(n : int):
        print("fibo({})を呼び出しました。".format(n))

        if n == 0: return 0
        if n == 1: return 1

        result =  fibo(n-2) + fibo(n-1)
        print("{}項目 = {}".format(n, result))

        return result
    
    n = int(input("n = "))
    print("result: {}".format(fibo(n)))

if __name__ == '__main__':
    main()