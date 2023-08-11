def main():
    n = int(input())
    a = list(map(int,input().split()))
    v = int(input())

    for i in range(n):
        if a[i] == v:
            found_index = i
    print(found_index)

if __name__ == '__main__':
    main()