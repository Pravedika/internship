def palindrome(num):
    if num == num[::-1]:
        print("palindrome number")
    else:
        print("not a palindrome")
palindrome(121)