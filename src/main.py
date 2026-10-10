from datetime import date
from utils import add, subtract, multiply, safe_calculate, divide

print("Khondoker Khalid Hasan")
print("Today's Date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))

print("Safe calculation:", safe_calculate("add", 10, 5))
print("Error test:", safe_calculate("add", 10, "hello"))

print("Division:", divide(10, 5))
print("Division error:", safe_calculate("divide", 10, 0))