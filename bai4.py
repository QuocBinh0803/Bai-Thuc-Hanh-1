def pascal(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomial_coefficient(line, i), end=" ")
        print()

def binomial_coefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def main():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("nhập số nguyên dương.")
        return
    pascal(n)

if __name__ == "__main__":
    main()