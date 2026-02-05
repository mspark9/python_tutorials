# default parameter
def my_func(country='korea'):
    print(f'I am from {country}')

# my_func()
# my_func('USA')

# collection parameter
def my_func_01(param):
    for x in param:
        print(x)

# my_func_01(['a', 'b', 'c'])
# my_func_01((1, 2, 3))

# prevent default parameter
def my_func_02(aaa, /):
    print(aaa)

# my_func_02(1)

# keyword only parameter
def my_func_03(*, bbb):
    print(bbb)

my_func_03(bbb=1)