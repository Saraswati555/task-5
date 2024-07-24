'''#question 1
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

"result - [10, 501, 22, 37, 100, 999, 87, 351]"

#Question 2
# Sample list containing integers and strings
my_list = [10, 'hello', 20, 'world', 30]

# Define a lambda function to check if an element is an integer or string
check_int_or_str = lambda x: all(type(element) in (int, str) for element in x)

# Use the lambda function to check the entire list
result = check_int_or_str(my_list)

# Print the result
if result:
    print("Every element in the list is an integer or string.")
else:
    print("Not every element in the list is an integer or string.")

#question 3
def fibonacci(count):
    fib_list = [0, 1]

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))

    return fib_list[:count]

print(fibonacci(50))'''

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test cases
print(validate_email("guvi@gmail.com"))  # True
print(validate_email("invalid-email"))         # False

def validate_bangladesh_mobile(mobile):
    pattern = r'^(?:\+88|88)?01[3-9]\d{8}$'
    return re.match(pattern, mobile) is not None

# Test cases
print(validate_bangladesh_mobile("+8801712345678"))  # True
print(validate_bangladesh_mobile("01712345678"))     # True
print(validate_bangladesh_mobile("0191234567"))      # False








