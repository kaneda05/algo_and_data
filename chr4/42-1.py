def main():
    n = int(input("n = "))
    memo = [-1] * (n+1)

    def tri(n: int):
        if n == 0 or n == 1: return 0
        if n == 2: return 1

        if memo[n] != -1:
            return memo[n]

        result = tri(n-1) + tri(n-2) + tri(n-3)
        memo[n] = result

        return result

    print("result : {}".format(tri(n)))

if __name__ == '__main__':
    main()
