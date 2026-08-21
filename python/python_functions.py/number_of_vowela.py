def vowels(s):
    count =0
    for x in s:
        if x in "aeiouAEIOU":
            count += 1
    return count
print(vowels("kiran"))