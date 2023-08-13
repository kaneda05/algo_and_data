def main():
    def func(n: int):
        print("func({})を呼び出しました。".format(n))
        if n == 0:
            return 0
        
        result = n + func(n-1)
        print("{}までの和 = {}".format(n, result))

        return result

    result = func(int(input('number:')))
    print("result: {}".format(result))

if __name__ == '__main__':
    main()