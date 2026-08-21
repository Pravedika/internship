def palindrome(string):
    if string == string[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome("madam"))