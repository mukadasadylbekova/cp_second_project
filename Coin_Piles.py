import sys
input = sys.stdin.read

def can_empty_piles(a, b):
    # Condition 1: Total coins must be divisible by 3
    if (a + b) % 3 != 0:
        return "NO"
    # Condition 2: Neither pile should have more than double the other
    if 2 * a < b or 2 * b < a:
        return "NO"
    return "YES"

def main():
    data = input().split()
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        results.append(can_empty_piles(a, b))
    
    # Output all results at once
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
