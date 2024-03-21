def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def neper(n):
    e_sum = 0
    for k in range(n + 1):
        a_k = 1 / factorial(k)
        e_sum += a_k
    return e_sum

def main():
    n = int(input("Nhập số nguyên n (n >= 0): "))
    if n < 0:
        print("Vui lòng nhập số nguyên không âm.")
        return
    print("Tổng của các số hạng a0 + a1 + ... + a", n, "là:", neper(n))

if __name__ == "__main__":
    main()
