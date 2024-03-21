def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
        return b

def main():
    n = int(input("Nhập số nguyên n (n >= 0): "))
    if n < 0:
        print("Vui lòng nhập số nguyên không âm.")
        return
    print("Số Fibonacci thứ", n, "sử dụng đệ qui là:", fibonacci_recursive(n))
    print("Số Fibonacci thứ", n, "không sử dụng đệ qui là:", fibonacci_iterative(n))

if __name__ == "__main__":
    main()
