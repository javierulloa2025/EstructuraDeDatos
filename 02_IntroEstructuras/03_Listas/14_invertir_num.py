def reverse_digits(num):
    sign = -1 if num < 0 else 1
    reversed_str = str(abs(num))[::-1]
    return sign * int(reversed_str)

print(reverse_digits(-9675))