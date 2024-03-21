def classify_number(n):
    divisor_sum = sum([i for i in range(1, n) if n % i == 0])
    if divisor_sum < n:
        return "deficient"
    elif divisor_sum == n:
        return "perfect"
    else:
        return "abundant"
def number(x, y):
    for num in range(x, y + 1):
        print("Số", num, "là", classify_number(num))
def main():
    x = int(input("Nhập số nguyên dương x: "))
    y = int(input("Nhập số nguyên dương y (x <= y): "))
    if x <= 0 or y <= 0 or x > y:
        print("Vui lòng nhập hai số nguyên dương sao cho x <= y.")
        return
    number(x, y)
if __name__ == "__main__":
    main()
