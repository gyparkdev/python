import math

def getArea(length):
  area = length * length * math.pi
  return area

value = input("Input a number : ")

area = getArea(int(value))

print("Input number : {0} => Area : {1}".format(value, area))