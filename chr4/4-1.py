def main():
    def func(n: int):
        return 0 if n == 0 else n + func(n - 1)

    result = func(int(input('number: ')))
    print('result: {}'.format(result))
    
if __name__ == '__main__':
    main()