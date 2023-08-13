def main():
    def GCD(m: int, n: int):
        if n == 0: return m

        return GCD(n, m % n)
        
    m = int(input("m:"))
    n = int(input("n:"))
    print(GCD(m,n))

if __name__ == '__main__':
    main()