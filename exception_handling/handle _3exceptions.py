try:
    a = int(input("enterthe value: "))
    result = 10 / a 
except ValueError:
    print("please enter the vaid number")
except NameError:
    print("please enter the valid number")
except ZeroDivisionError:
    print("division by zero is not allowed")