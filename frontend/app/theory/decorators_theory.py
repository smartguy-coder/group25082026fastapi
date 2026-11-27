# from dis import dis
#
def foo():
    print(1666666)
    print(65656666666666666)
#
#
#
# print(22222)
# foo()
# # dis(foo)
#
# print(foo                                     )
# # <function foo at 0x000001DBE90E3240>
#
# foo.number = 5
# foo.number2 = 50
# print(foo.__dict__)
#
# something = print
# print(id(      print    ))
# print(id(      something    ))
# print(id(      foo        ))
#
# something(999999999999999999999)

print(id(foo))

def foo_level_up(function):
    def wrapper():
        print('I have got function', function)
        print('before')
        function()
        print('after')

    return wrapper


foo = foo_level_up(function=foo                      )
# foo_level_up(function=print                      )

print(foo)
foo()
foo()



print(id(foo))







