def is_factorial(x):
    if x < 1:
        return False
    i = 1
    fact = 1
    while fact < x:
        i += 1
        fact *= i
    return fact == x
print(is_factorial(24))   
print(is_factorial(145)) 

# palindrome check 
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
n = 121
print(is_palindrome(n))


def char_counts_ordered(s):
    counts = {}
    order = []
    for ch in s:
        if ch == ' ':
            continue
        if ch not in counts:
            order.append(ch)
            counts[ch] = 1
        else:
            counts[ch] += 1

    return ' '.join(f"{ch}{counts[ch]}" for ch in order)

print(char_counts_ordered("aaa bb caab"))

