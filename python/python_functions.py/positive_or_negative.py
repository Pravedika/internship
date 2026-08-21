def is_positive(n):
    if n > 0:
        return "positivr number"
    elif n < 0:
        return "negative number"
    else:
        return "zero"
result = is_positive(-8)
print(result)