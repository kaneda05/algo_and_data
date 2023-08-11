def main():
    n = int(input())
    a = list(map(int,input().split()))
    v = int(input())

    flag = False
    for i in range(n):
        if a[i] == v:
            flag = True

    if flag: print("Yes")
    else: print("No")

if __name__ == '__main__':
    main()