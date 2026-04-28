# =========================
# 1. FizzBuzz
# =========================
def fizzbuzz(N):
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# =========================
# 2. Slope of a Line
# =========================
def slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Undefined"
    return round((y2 - y1) / (x2 - x1), 2)

# =========================
# 3. Count Digits
# =========================
def count_digits(N):
    return len(str(abs(N)))

# =========================
# 4. Reverse String
# =========================
def reverse_string(S):
    return S[::-1]   # or loop version if needed

# =========================
# 5. Count Primes in Range
# =========================
def count_primes(L, R):
    sieve = [True] * (R+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(R**0.5)+1):
        if sieve[i]:
            for j in range(i*i, R+1, i):
                sieve[j] = False
    return sum(1 for i in range(L, R+1) if sieve[i])

# =========================
# 6. Number Pyramid
# =========================
def number_pyramid(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

# =========================
# 7. Strictly Decreasing Digits
# =========================
def strictly_decreasing(L, R):
    count = 0
    for num in range(L, R+1):
        s = str(num)
        valid = True
        for i in range(len(s)-1):
            if s[i] <= s[i+1]:
                valid = False
                break
        if valid:
            count += 1
    return count

# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    # Uncomment the function you want to test
    # fizzbuzz(15)
    # print(slope(2, 3, 6, 7))
    # print(count_digits(-9876))
    # print(reverse_string("python"))
    # print(count_primes(10, 30))
    # number_pyramid(4)
    # print(strictly_decreasing(10, 50))
    pass