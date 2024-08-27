import math
print('########################################### 1- Variables ########################################################')
students_count = 1000
rating = 4.99  # float
is_published = True
course_name = "Python Programming"
print('######################################### 3- Strings ########################################################')
course = '''this is a long string'''
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])  # substring index 0,1,2
print(course[0:])  # to end
print('######################################## 4- Escape Sequences 转义序列 ###########################################')
# \"
# \'
# \\
# \n
print('############################### 5- Formatted Strings ########################################################')
first = "Ching"
last = "Yip"
full_1 = first + ' ' + last
full_2 = f"{first} {last}"
full_3 = f"{len(first)} {2 + 2}"
print(full_3)
print("############################### 6- String Methods ########################################################")
course = "Python Programming"
""" .upper() won't change the origin string, it will return a new string """
course_capital = course.upper()
print(course.upper())
print(course.lower())
""" chang the all lower case string to first letter upper case: "python programming" to "Python Programming" """
print("python programming".title())
""" strip remove the blank space on both the beginning and end of a string """
print(" python ")
print(" python ".strip())
print(" python ".lstrip())
print(" python ".rstrip())
""" find the index of a string """
print("python programming".find("pro"))
print('############################### 7- Numbers ########################################################')
x = 1
x = 1.1
x = 1+2j

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)     # 3.3333333335
print(10 // 3)    # 3
print(10 % 3)
print(10 ** 3)

x = 10
x = x+3
x += 3
print('############################### 8- Working with Numbers ########################################################')
print(round(2.9))   # 3
print(abs(-2.9))    # 2.9

""" search on google ---> python 3 math module ---> more math functions """
print(math.ceil(2.2))  # 3
print('############################### 9- Type Conversion ########################################################')
x = input('x: ')
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)
