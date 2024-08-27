from array import array
from collections import deque
from sys import getsizeof
from pprint import pprint
print(
    '############################### 1- Lists ########################################################')
# every object in a list can be of a different type, so they don't have to be from the same type
letters = ["a", "b", "c"]
zeros = [0]*5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))
print('############################### 2- Accessing Items ########################################################')
letters = ["a", "b", "c", "d"]
print(letters[0])
print(letters[-1])

letters[0] = "A"
print(letters[0:3])
# get a copy of the original list: letters[:]

numbers = list(range(20))

print(numbers[::2])
# step of 2: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[0:3:2])
# [0, 2]
print(numbers[::-1])
# in verse order
print('############################### 3- List Unpacking ########################################################')
numbers = [1, 2, 3, 4, 5]
first, second, *other = numbers
print('############################### 4- Looping over Lists ########################################################')
letters = ["a", "b", "c", "d"]
for letter in enumerate(letters):
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')
    print(letter)
    # 0
    # 1
    # 2
    print(letter[0])
    # a
    # b
    # c
    print(letter[1])
for index, letter in enumerate(letters):
    print(index, letter)
print('############################### 5- Adding or Removing Items ########################################################')
letters = ["a", "b", "c"]
# Add
letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
letters.pop(0)
# remove an object but you don't know the index
letters.remove("b")
# delete a range of items
del letters[0:3]
letters.clear()
print(letters)
print('############################### 6- Finding Items ########################################################')
letters = ["a", "b", "c"]
print(letters.index("a"))
if "d" in letters:
    print(letters.index("d"))
# for the object which maybe not in the list
print(letters.count("d"))
print('############################### 7- Sorting Lists ########################################################')
numbers = [3, 51, 2, 8, 6]
# will change the original list
numbers.sort()
numbers.sort(reverse=True)
# won't change the origin list
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

# how about sort complex list, a list of tupple
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
print('############################### 8- Lambda Functions ########################################################')
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# one line anonymous function
# items.sort(key=lambda parameter: expression)
items.sort(key=lambda item: item[1])
print(items)
print('############################### 9- Map Function ########################################################')
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# method one
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# method two, map function takes two parameters, a function(lambda) and an iterable(items)
# map() 函数会将 function 应用到 iterable 中的每个元素，并返回一个可迭代的结果对象，这个结果对象可以通过 list()、tuple() 等函数转换为列表、元组等数据结构。
x = map(lambda item: item[1], items)
print(x)
for item in x:
    print(item)

# method three
prices = list(map(lambda item: item[1], items))
print(prices)
print('############################### 10- Filter Function ########################################################')
x = list(filter(lambda item: item[1] >= 10, items))
print(x)
print('############################### 11- List Comprehensions ########################################################')
# Comprehensions 用于创建新的可迭代对象（例如列表、字典、集合等），通常是基于现有的可迭代对象进行变换或筛选。
prices = [item[1] for item in items]
print(prices)
filtered = [item for item in items if item[1] >= 10]
print(filtered)
print('############################### 12- Zip Function ########################################################')
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))
print('############################### 13- Stacks ########################################################')
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
# 0, "", [] falsy value
if not browsing_session:
    print("redirect", browsing_session[-1])
print('############################### 14- Queues ########################################################')
# from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)
queue.pop()
print(queue)
if not queue:
    print("empty")
print('############################### 15- Tuples ########################################################')
point = 1, 2
point = 1,
point = ()
print(type(point))
# result: (1, 2, 3, 4)
point = (1, 2) + (3, 4)
print(point)
# result: (1, 2, 1, 2, 1, 2)
point = (1, 2) * 3
print(point)
point = tuple([1, 2])
print(point)
point = tuple("Hello World")
print(point)
print(point[0:2])
point = 1, 2, 3
x, y, z = point
if 10 in point:
    print("exists")

# TypeError: 'tuple' object does not support item assignment
# point[0] = 10
print('############################### 16- Swapping Variables ########################################################')
x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)

x, y = y, x
print("x", x)
print("y", y)
print('############################### 17- Arrays ########################################################')
# from array import array

# the first parameter is typecode, which is a string that determines the type of objects in your array
# on google search python 3 typecode. i is for signed integer
numbers = array("i", [1, 2, 3])
print('############################### 18- Sets ########################################################')
# set: a collection with no duplicates, unordered, we cannot access sets using index
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

second = {1, 4}
second.add(5)
second.remove(5)
len(second)

first = set([1, 1, 2, 3, 4])
second = {1, 5}
# union: either in the first or in the second
print(first | second)
# intersection: both in the first and second
print(first & second)
# the difference between two sets
print(first - second)
# semantic difference, ^ is carrot, either in the first or second sets but not both
print(first ^ second)

if 1 in first:
    print("yes")
print('################################################# 19- Dictionaries ########################################################')
# Dictionaries: a collection of key/value pairs
# list()
# tuple()
# set()
# dict()
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)

# methond 1:
if "a" in point:
    print(point["a"])
# methond 2:
# if you don't have key 'a', return 0 by default
print(point.get("a", 0))

del point["x"]
print(point)

# method 1 for loop a dict:
for key in point:
    print(key, point[key])

# method 2 for loop a dict:
for key, value in point.items():
    print(key, value)
print('################################################# 20- Dictionary Comprehensions ########################################################')
# we can use comprehensions with lists, sets and dictionaries
# [expression for item in items]

# set:
#  method 1:
values = []
for x in range(5):
    values.append(x*2)
print(values)

#  method 2:
values = [x*2 for x in range(5)]
print(values)

# dict:
#  method 1:
values = {}
for x in range(5):
    values[x] = x*2
print(values)

#  method 2:
values = {x: x*2 for x in range(5)}
print(values)
print('################################################# 21- Generator Expressions ########################################################')
# from sys import getsizeof

# we created a list using a list comprehension expression, then we iterate over all the numbers in this list
# but if we are working with really large data set, in this case, we shouldn't store all the data in the memory. we should use a generator object
values = [x*2 for x in range(10)]
for x in values:
    print(x)

# generator object: iterable, just like list, we can iterate over them, and in each iteration, we generat or spite out a new value. unlike lists, they don't store all the values and memory, they generate a new value in each iteration
# we get the same exact result, however values is no longer a list, it is a generator object
# generator object is iterable, and in each iteration they spit out a new value
values = (x*2 for x in range(10))
for x in values:
    print(x)

# size
values_object = (x*2 for x in range(10000))
# size of generator object: 112
# generator object takes 112 bytes of memory
print("size of generator object: ", getsizeof(values_object))
values = [x*2 for x in range(10000)]
print("size of list: ", getsizeof(values))

# len of generator object will have an error: TypeError: object of type 'generator' has no len()
# print(len(values_object))
print('################################################# 22- Unpacking Operator ########################################################')
numbers = [1, 2, 3]

# the same exact result
# unpacking operator, the same as ... in JavaScript
print(*numbers)
print(1, 2, 3)

values = list(range(5))
values = [*range(5), *"Hello"]
# [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# we can also unpack dict but we need to use **
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
# {'x': 10, 'y': 2, 'z': 1}
print(combined)

# we can use the unpacking operator to take out individual values in any iterable

print('################################################# 23- Exercise ########################################################')
# find most repeated character in this text
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)
# sorted(): this function takes an iterable
# .items() returns all the key value pairs as a list of tuples, which can be sorted
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print("result: ", char_frequency_sorted[0])
