if __name__ == "__main__":
    def decorator(fn):

        def wrapper(*args, **kwargs):
            for index1, value1 in enumerate(args):
                try:
                    next(iter(value1))
                except TypeError:
                    raise TypeError(F"объект {value1} по индексу {index1}")

            for index, value in kwargs.items():
                try:
                    next(iter(value))
                except TypeError:
                    raise TypeError(F"объект{value} по индексу {index}")
            result = fn()
            return result
        return wrapper


    @decorator
    def hi(*args, **kwargs):
        ...


    hi([1, 2, 3], b=(i for i in range(10)))
