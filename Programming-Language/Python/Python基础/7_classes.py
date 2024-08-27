from collections import namedtuple
from abc import ABC, abstractmethod
print(
    '################################################# 2- Creating Classes ########################################################')


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
print('################################################# 3- Constructors ########################################################')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()
print('################################# 4- Class Attributes vs Instance Attributes ################################################')


class Point:
    # default_color is class level variable, it shared by all instances
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# instance attributes
point = Point(1, 2)
point.z = 10
# red
print(point.default_color)
# red
print(Point.default_color)
# 10
print(point.z)


Point.default_color = "yellow"
another = Point(3, 4)
# yellow
print(another.default_color)
# yellow
print(point.default_color)
print('########################################## 5- Class Methods vs Instance Methods ####################################')


'''
    静态方法
    @staticmethod
    静态方法其实与这个类没关系,他仅仅是一个函数,只不过,这个函数被定义在了类的范围之内
    staticmethod 不会传入 cls
    staticmethod 的适用范围: 工具类,工具方法,不需要使用这个类的实例变量和实例属性
'''
class Student:
    school = "abc"

    @classmethod
    def hello(cls):
        print(f"hello {cls.school}")

    @staticmethod
    def out():
        print(f"hello {Student.school}")

    @staticmethod
    def size(value: int) -> float:
        return value * 1.5

    def speak(self):
        n = 12
        # n = Student.size(n)    # 利用 Student.size(n) 调用 staticmethod
        n = self.size(n)         # 直接调用这个类中的方法
        print(n)


def main():
    Student.hello()
    print(Student.school)
    Student.out()

    Student().speak()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()
print('########################################## 6- Magic Methods ########################################################')
# Magic Methods: __methodname__, they are called by python interpreter automatically, depending on how we use our objects and classes
# for example, __init__ method, when we create a new point object, this method will be called automatically
# google: python 3 magic methods

# __str__: when we try to convert an object to a string
# print(point):
# <__main__.Point object at 0*107330208>: this is the default implementation of the str method in the point object
# __main__: the name of the module
# Point object: followed by the class name
# 0*107330208: and the address of this point object in memory


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # over write __str__ method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
# the same result:
print(str(point))
print('################################################# 7- Comparing Objects ########################################################')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
# python will automatically figure out what to do if you use the less than operator
print(point < other)
print('########################################## 8- Performing Arithmetic(算数) Operations ############################################')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x)
print('########################################## 9- Making Custom Containers ############################################')


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # if not re-write the following method, cloud["python"] will throw error
    # if we don't have the python tag, dictionary would throw an error
    def __getitem__(self, tag):
        # if don't have it, return 0 by default
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
print(cloud["python"])
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(cloud["python"])

# re-write set item
cloud["python"] = 10
print(cloud.tags)

len(cloud)

################################################################################################################################################
# - sets, lists, dicts: they are data structures or container types
# - how about create your own custom container types, keep tack of the number of various tags in a blog. for example, how many articales do we have that are tagged with python or js
# - becaue the class is a container, it supports various operators around containers

cloud = TagCloud()
# get the number of items in this container
len(cloud)
# get an item by it's key
cloud["python"] = 10
for tag in cloud:
    print(tag)

print('########################################## 10- Private Members ############################################')


class TagCloud:
    def __init__(self):
        # use F2 to refactor the variable to a class private variable
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")

# result: 3
print(cloud["PYTHON"])

# result: KeyError: 'PYTHON'
# if we access the underline dictionary in this class
# because we don't have 'PYTHON' key in the dictionary, everything is stored in a lower case
# so the problem with this class is that it gives us access to the underline dictionary that is used to keep track of the count of text
# to fix this problem, we need to hide this attribute from the outside, so we cannot access it
print(cloud.tags["PYTHON"])

# this is the dictionary that holds all the attributes in the class
# result: {'_TagCloud__tags': {'python': 3}}
# in this class, we have this attribute called _TagCloud__tags. so when python interpreter runs this code, it automatically rename this attribute and prefix it wiht the name of its class, technically we can still access it
print(cloud.__dict__)
print(cloud._TagCloud__tags)
print('########################################## 11- Properties ############################################')
# method zero: 
class Product:
    def __init__(self, price):
        self.price = price

product = Product(-50)

# method one: 通过使用setter getter方法来阻止外部错误修改. 在setter中设置一些error handler. 这会形成一个新问题:如果在没有 setter getter的原本class中,已经有被使用过,已经有 product.price = 3 这个方式设置 price 的 case,那么 setter getter 的修改就会需要改很多地方,将所有 product.price = 3 都改成 product.set_price(3)
# method two: 引入property ---> 可以正常使用product.price = 1 以及 print(product.price)
# method three：明明已经有了属性/set/get方法，还要再加property 类，感觉很冗余。就产生了使用@property装饰器的场景。

# method one: this code or this implementation is not pythonic, which is not using python best practice, is kind of code that a java programmer learning python would write


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(-50)
price = product.get_price()
""" 
在Python中, 私有变量（以双下划线开头的变量）实际上只是一种命名约定, 而不是严格意义上的私有变量。Python解释器会对双下划线开头的变量名进行名称修饰(name mangling), 将其改写为_ClassName__variable的形式, 但这只是一种名称变换, 而不是访问控制。

因此, 虽然__price被认为是私有变量, 但仍然可以通过_ClassName__price的方式来访问它。在你的例子中, get_price()方法正是通过这种方式来获取__price的值, 因此你能够成功打印出价格。

不过, 即便是这样, 开发者一般还是遵循约定, 不直接通过名称变换的方式去访问私有变量, 而是使用提供的公共接口, 比如get_price()方法。
"""
print(price)
# method two: we use property, which is an object that sits in front of an attribute and allows us to get or set the value of that attribute


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
# a property looks like a regular attribute from the outside, but internally it has two methods that we call a getter and a setter
product.price = -1
print(product.price)


# now while these price properties solve our problem, the two methods we wrote are still accesssible


class Product:
    def __init__(self, price):
        # we can use our price property like a regular attribute
        self.price = price

    @property
    def price(self):
        return self.__price

    # if we comment out this method, the property will be read only
    # with these two decorators, we can easily create a property
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


# for test property itself
product = Product(-10)
print(product.price)


# for test read only property
# result: AttributeError: can't set attribute
product = Product(10)
product.price = 2
print(product.price)


print('########################################## 12- Inheritance ############################################')


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print('########################################## 13- The Object Class ############################################')
# Animal inherits from another class called object
# we have a class called object, and that is the base class for all classes in Python
# every class that we have in Python directly or indirectly derives from the object class
print('########################################## 14- Method Overriding ############################################')


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # method overriding: replace a method in the base class
    def __init__(self):
        # super() to get access to the super or base class, which is in this case Animal
        super().__init__()
        print("Mammal Constructor")
        self.weiht = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weiht)
print('########################################## 15- Multi-level Inheritance ############################################')
# if you should use inheritance, limit it to one or two levels
print('########################################## 16- Multiple Inheritance ############################################')


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
# first it looks at the manager class to see if it has a method called greet, if it doesn't, it will look at it's first base class, does employee has a greet method
manager.greet()


# good example of Multiple Inheritance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


print('########################################## 17- A Good Example of Inheritance ############################################')
# you want to model the concept of a stream of data, we can read a stream of data from a file, from a network, or from the memory, all these streams have a few things in common. we can open them, we can close them, we can read data from them, but how we read data is dependent upon the type of stream, because reading data from a file is different than reading it from a network


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


print('########################################## 18- Abstract Base Classes ############################################')
# an abstract base class is like a half baked cookie, it's not ready to be eaten, its purpose is to provide some common code to these derivities
# from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")

    # if class derives from the stream class, it has to implemnet this method, otherwise that class will also be considered abstract
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    pass


stream = Stream()
stream.open()

# if MemoryStream didn't implemnet method read, stream_2 will be considered as abstract class too
# TypeError: Can't instantiate abstract class MemoryStream with abstract method read
stream_2 = MemoryStream()
stream_2.open()
print('########################################## 19- Polymorphism ############################################')
# Polymorphism: many forms


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(ui_control):
    ui_control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
draw(ddl)

textbox = TextBox()
draw(textbox)


def draw_2(ui_controls):
    for ui_control in ui_controls:
        ui_control.draw()


ddl = DropDownList()
textbox = TextBox()
draw_2([ddl, textbox])
print('########################################## 21- Extending Built-in Types ############################################')


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append('1')
print('########################################## 22- Data Classes ############################################')
# from collections import namedtuple
# 使用namedtuple代替只包含attribute不包含方法的类

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=10, y=2)
p1 = Point(x=1, y=2)
print(p1.x)
p2 = Point(x=1, y=2)
print(p1 == p2)
