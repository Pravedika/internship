def grade(marks):
    if marks<100 and marks>=85:
        print("Grade-A")
    elif marks<85 and marks>=65:
        print("Grade-B")
    elif marks<65 and marks>=55:
        print("Grade-C")
    elif marks<55 and marks>=35:
        print("Grade -D")
    else:
        print("Failed")
grade(64)
