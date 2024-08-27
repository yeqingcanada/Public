from enum import Enum

class Gender(Enum):
  MALE = 1
  FEMALE = 2

class Student:
  def __init__(self, gender: Gender):
    self.gender = gender

def main():
  print(type(Gender.MALE))
  print(Gender.MALE.name)
  print(Gender.MALE.value)

  student = Student(Gender.FEMALE)

  if student.gender == Gender.MALE:
    print('male')
  else:
    print('female')

if __name__ == '__main__':
  main()