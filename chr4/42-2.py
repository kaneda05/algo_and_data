def main():
    from functools import lru_cache
    n = int(input("n = "))

    @lru_cache
    def tri(n: int):
        if n == 0 or n == 1: return 0
        if n == 2: return 1
        result = tri(n-1) + tri(n-2) + tri(n-3)
        return result
    
    for i in range(n+1):
        print('n : {:2d}, result: {:10d}'.format(i, tri(i)))
if __name__ == '__main__':
    main()