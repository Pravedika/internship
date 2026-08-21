def duplicate(numbers):
    result = []
    for x in numbers:
        if x not in result:
            result.append(x)
    return result
numbers = [10,20,30,12,10,30,20,12,45]
print(duplicate(numbers))
