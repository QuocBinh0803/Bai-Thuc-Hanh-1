def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def gcd_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def main():
    m = int(input("Nhập số nguyên dương m: "))
    n = int(input("Nhập số nguyên dương n: "))
    if m <= 0 or n <= 0:
        print("Vui lòng nhập hai số nguyên dương.")
        return
    print("Ước số chung lớn nhất của", m, "và", n, "sử dụng đệ qui là:", gcd_recursive(m, n))
    print("Ước số chung lớn nhất của", m, "và", n, "không sử dụng đệ qui là:", gcd_iterative(m, n))

if __name__ == "__main__":
    main()

    
    