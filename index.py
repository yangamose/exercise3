def greet(firstname,lastname):
    print('this is greet function. welcome' + firstname +' '+ lastname +'!')
greet('yanga' ,' mose')

def personalized_greeting(name):
    print(f"hello,{ name}")

personalized_greeting("yanga")

def square(number):
    return number * number
result = square(5)
print(result)

def rectangle_area(length, width):
    return length * width
print(rectangle_area(4, 5))

def apply_operation(func, number):
    return func(number)
def double(number):
    return number * 2
print(apply_operation(double, 7))
print(apply_operation(square, 3))