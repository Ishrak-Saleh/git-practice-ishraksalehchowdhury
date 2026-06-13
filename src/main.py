from datetime import date
from utils import add, subtract, multiply, divide

print("My name is Ishrak")
print("Today's date is:", date.today())

print("5 + 3 =", add(5, 3))
print("5 - 3 =", subtract(5, 3))
print("5 x 3 =", multiply(5, 3))
print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))