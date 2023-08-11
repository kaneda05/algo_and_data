def main():
    n = int(input())
    a = list(map(int,input().split()))
    min_value1 = float('inf')
    for i in range(n):
        if a[i] < min_value1:
            min_value1 = a[i]
    
    min_value2 = float("inf")
    for i in range(n):
        if a[i] == min_value1: continue

        if a[i] < min_value2:
            min_value2 = a[i]
    
    print(min_value2)

if __name__ == '__main__':
    main()