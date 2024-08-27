from timeit import timeit
print('################################################# 2- Handling Exceptions ########################################################')
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")
print('################################################# 3- Handling Different Exceptions ########################################################')
try:
    age = int(input("Age: "))
    cfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exceptions were thrown.")

# handle multiple error at the same time, except block will be excute only one, which means one of them execute the other won't be executed
try:
    age = int(input("Age: "))
    cfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print('################################################# 4- Cleaning Up ########################################################')
# 如果要关闭文件，但是之前有几步，其中有error，那么文件就关不上。应该把关闭文件的语句方法finally中，finally中的语句是一定会执行的
try:
    file = open("5_data _structures.py")
    age = int(input("Age: "))
    cfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
print('################################################# 5- The With Statement ########################################################')
# if an object, supports the context management protocol, if an object has these two methods, enter and exit. file.__exit__ we can use the object with the with statement
try:
    with open("./5_data _structures.py") as file, open("./4_functions.py") as file2:
        print("File opened.")
    age = int(input("Age: "))
    cfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print('################################################# 6- Raising Exceptions ########################################################')
# google: python 3 built-in exceptions


def calculate_sfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_sfactor(-1)
except ValueError as error:
    print(error)
print('################################################# 7- Cost of Raising Exceptions ########################################################')
# 没事不要使用raise，耗时
code1 = """
def calculate_sfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_sfactor(-1)
except ValueError as error:
    pass
"""
code2 = """
def calculate_sfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_sfactor(-1)
if xfactor == None:
    pass
"""

print("first code =", timeit(code1, number=10000))
print("second code =", timeit(code2, number=10000))
