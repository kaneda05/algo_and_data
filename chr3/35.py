def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    while all([True if i % 2 == 0 else False for i in a]):
        cnt += 1
        a = [i/2 for i in a]
    
    print(cnt)

if __name__ == '__main__':
    main()