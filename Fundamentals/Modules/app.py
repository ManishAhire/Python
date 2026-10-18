import addition  # Custome Module

# rename module
import addition as Add

import math  # inbuilt Module

# from...import
from math import pi

result = Add.addTwoNumbers(10, 20)
print("\nAddition of two numbers is: ", result)

print("\nValue of PI: ", math.pi)
print("\nfrom...import PI: ", pi)
