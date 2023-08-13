def main():
    F = [0, 1]
    k = int(input('number = '))
    for i in range(2, k+1):
        F.append(F[i-1] + F[i-2])
        print("{}項目: {}".format(i, F[i]))
    
    print("result : {}".format(F[-1]))


if __name__ == '__main__':
    main()