def main():
    s = input()
    n = len(s)
    ans = 0

    for bit in range(1<<(n-1)):
        formula = s[0]
        for i in range(n-1):
            if ((bit>>i)&1) == 1:
                formula += "+"
            formula += s[i+1]
        #print(formula)
        ans += eval(formula)
    
    print(ans)

if __name__ == "__main__":
    main()