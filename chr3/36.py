def main():
    k, n = map(int,input().split())
    cnt = 0
    for x in range(k+1):
        for y in range(k+1):
            if 0<=n-x-y<=k:
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()