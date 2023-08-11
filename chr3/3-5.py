def main():
    n = int(input())
    a = list(map(int,input().split()))
    w = int(input())

    flag = False
    for bit in range(1<<n):
        cal = 0
        for i in range(n):
            # 整数bitの表す部分集合にi番目の要素が含まれる場合
            if bit&(1<<i):
                cal += a[i]
        
        if cal == w:
            flag = True
            break
    
    if flag: print("Yes")
    else: print("No")

if __name__ == '__main__':
    main()