from functools import wraps


def round_result(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(*args)
        print(args)
        print(kwargs)
        print('I have got function', function)
        print('before')
        result = function(*args, **kwargs)
        print('after')
        result = round(result, 4)
        return result
    # wrapper.__name__ = 'kfjghjkhbbkffgbf'
    return wrapper

def round_result_parametrized(precision: int = 3):
    def round_result_inner(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            print('before')
            result = function(*args, **kwargs)
            print('after')
            result = round(result, precision)
            return result
        return wrapper
    return round_result_inner


@round_result_parametrized(precision=6)
# get_pi = round_result ( get_pi )
def get_pi() -> float:
    """some info about PI"""
    return 3.1415926536


@round_result_parametrized(precision=1)
def divide_by_3(number: int | float) -> float:
    result = number / 3
    return result

@round_result
def multiply_2_numbers(number1: int | float, number2: int) -> float:
    result = number1 * number2
    return result

@round_result
def divide_2_numbers(dividend: int | float, divisor: float) -> float:
    quotient = dividend / divisor
    return quotient


print(get_pi)
# get_pi.__name__ = "bla_bla"
# print(get_pi.__name__)
# print(get_pi.__doc__)
#
#
rres = get_pi()
print(rres)
#
rres = divide_by_3(12.6565)
print(rres)
#
# rres = multiply_2_numbers(12.6565, number2=55)
#
# print(rres)
#
# rres = divide_2_numbers(divisor=12.6565, dividend=55)
#
# print(rres)