print('############################### 4- Keyword Arguments ########################################################')
# for more readable code


def increment(number, by):
    return number + by


# by=1 is Keyword Arguments, 关键字参数 VS. 位置参数，关键字参数使我们可以打乱传参顺序
print(increment(2, by=1))
print('############################### 5- Default Arguments ########################################################')


def increment(number, by=1):
    # number is required parameter, by is optional parameter
    # all the required parameter should be in front of optional parameters
    return number + by


print(increment(2))
print('############################### 6- xargs ########################################################')
# there are times that I want to create a function that takes a variable number of arguments
# *args VS. **kwargs


def multiply(x, y):
    return x * y


# only two parameter is allowed here, we need to use * to pass variable numbers of arguments
multiply(2, 3, 4, 5)


def multiply_2(*numbers):
    print(numbers)


multiply_2(2, 3, 4, 5)
print('############################### 7- xxargs ########################################################')


def save_user(**user):
    # ** passing multiple key word arguments
    # python automatically package the mutiple key word argument into a dict
    # the result is dict, key : value pairs
    print(user)


save_user(id=1, name="John", age=22)
