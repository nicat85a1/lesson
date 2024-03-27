"""
num = int(input("Enter a number: "))
if num ** 0.5 % 1 == 0:
    print(f"The square root of the number is: {num**0.5:.0f}")
else:
    print("The number is not a perfect square.")
"""
"""
# task 1 lambda
square_root = lambda num: f"The square root of the number is: {num**0.5:.0f}" if num ** 0.5 % 1 == 0 else "The number is not a perfect square."
num = int(input("Enter a number: "))
print(square_root(num))
"""

"""
def exponent_function(nums):
    return [num**2 for num in nums]

nums = [1, 2, 3, 4, 5]

print("squares of numbers:", exponent_function(nums))
"""

# task 2 lambda
exponent = lambda nums: [num**2 for num in nums]

nums = [1, 2, 3, 4, 5]

print("squares of numbers:", exponent(nums))