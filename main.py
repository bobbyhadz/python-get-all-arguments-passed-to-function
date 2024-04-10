# Get all arguments passed to a Function in Python

def func(first, *args, **kwargs):

    # 👇️ ['first', 'args', 'kwargs']
    print(list(locals().keys()))

    all_arguments = locals()

    # 👇️ {'first': 'hello', 'args': ('arg1', 'arg2'), 'kwargs': {'name': 'bobby', 'age': 30}}
    print(all_arguments)

    my_variable = 'bobbyhadz.com'

    # 👇️ {'first': 'hello', 'args': ('arg1', 'arg2'), 'kwargs': {'name': 'bobby', 'age': 30}, 'all_arguments': {...}, 'my_variable': 'bobbyhadz.com'}
    print(locals())


func('hello', 'arg1', 'arg2', name='bobby', age=30)