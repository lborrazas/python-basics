import time
import math
import numpy


def calculate_time(real_function):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def wrapper(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        a = real_function(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", real_function.__name__, end - begin)
        return a

    return wrapper


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(4)
    print(math.factorial(num))


def falseDecorator(real_function):
    def falsy():
        print(4)

    return falsy


@calculate_time
def assignableFunction(val):
    return val


# calling the function.
@falseDecorator
def hello():
    print('hello')


if __name__ == '__main__':
    factorial(10)
    hello()
    a = assignableFunction('santiago')
    print('hola, {}'.format(a))

    a = numpy.array([1, 2, 3, 4, 5])
    print(type(a))

# LESSON: DECORATORS ARE f = decorator(f) and if they dont return what f returns then it does not work properly (if we wanted that)
