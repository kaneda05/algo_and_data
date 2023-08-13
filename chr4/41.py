def main():

    def tri(n: int):
        if n == 0 or n == 1: return 0
        if n == 2: return 1

        result = tri(n-1) + tri(n-2) + tri(n-3)
        return result

    n = int(input("n = "))
    print("result : {}".format(tri(n)))

if __name__ == '__main__':
    main()
