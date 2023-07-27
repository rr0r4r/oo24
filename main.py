import math
import datetime

def area(r, alpha):
  return math.pi * r**2 * math.degrees(alpha) / 360

def weekday(y, m, d):
  date = datetime.datetime(y, m, d).weekday()
  week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
  return week[date]
  
print(weekday(2023, 7, 21))


def arabNum(n):
  nn = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
  }
  new = ''
  for value, symbol in nn.items():
    while n >= value:
      new += symbol
      n -= value
    
  return new
print(arabNum(800))