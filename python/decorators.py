from functools import wraps

class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print(1, args)
        result = self.func(*args)
        print(ressult)
        print(4)
        return result

def decorator(function):
    @wraps(function) # Required to get the correct __name__
    def wrapper(*args, **kwargs):
        print(1)
        result = function(*args, **kwargs)
        print(3)
        return result
    return wrapper

def decorator_factory(factory_argument):
    def decorator(function):
        @wraps(function) # Required to get the correct __name__
        def wrapper(*args, **kwargs):
            print(f'Print: {factory_argument} from wrapper before decorated_function')
            result = function(*args, **kwargs)
            print(f'Print: {factory_argument} from wrapper after decorated_function')
            return result
        return wrapper
    return decorator

@decorator_factory('factory_argument')
def decorated_by_decorator_factory(method_argument):
    print(method_argument)
    return 2

@decorator
def decorated_by_single_decorator(method_argument):
    print(method_argument)
    return 2

@ClassDecorator
def foo(bar):
    return 7

if __name__ == '__main__':
    print('decorated_by_decorator_factory:')
    ressult = decorated_by_decorator_factory(method_argument='method_argument')
    print(f'return value: {ressult}')
    print(decorated_by_decorator_factory.__name__, '\n\n')

    print('decorated_by_single_decorator:')
    result = decorated_by_single_decorator(method_argument=2)
    print(f'return value: {ressult}')
    print(decorated_by_single_decorator.__name__)


    print(foo('bar'))