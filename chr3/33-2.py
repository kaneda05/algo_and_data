def main():
    n = int(input())
    a = list(map(int,input().split()))
    min_value1 = float('inf')
    min_value2 = float('inf')

    for i in range(n):
        # 最小値の更新
        if a[i] < min_value1:
            min_value2 = min_value1 # 最小値と仮置きしていた値が更新されたので2番目に代入
            min_value1 = a[i]

        # 2番目の最小値の更新
        elif a[i] < min_value2:
            min_value2 = a[i]
    
    print(min_value2)

if __name__ == "__main__":
    main()
