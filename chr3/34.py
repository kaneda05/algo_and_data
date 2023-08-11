def main():
    n = int(input())
    a = list(map(int,input().split()))
    max_value = float('-inf')
    min_value = float('inf')
    for i in range(n):
        if a[i] < min_value:
            min_value = a[i]
        
        if max_value < a[i]:
            max_value = a[i]
    
    max_diff = max_value - min_value
    print(max_diff)

if __name__ == '__main__':
    main()