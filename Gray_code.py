n = int(input())

# Generate Gray code for all numbers from 0 to 2^n - 1
for i in range(1 << n):  # 1 << n is 2^n
    gray = i ^ (i >> 1)  # Gray code formula
    # Format as binary with leading zeros to ensure length n
    print(format(gray, f'0{n}b'))
