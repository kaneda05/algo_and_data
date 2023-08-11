def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    k = int(input())

    min_value = float("inf")
    for i in range(n):
        for j in range(n):
            # 和がk未満ならば捨てる
            if a[i]+b[i] < k: continue

            # 最小値の更新
            if a[i]+b[j] < min_value:
                min_value = a[i]+b[i]
    
    print(min_value)

if __name__ == '__main__':
    main()
