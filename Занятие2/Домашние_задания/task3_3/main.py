def iter_arguments(fn):
    def wrapper(*args, **kwargs):
        print(*args)
        try:
            iter(*args)
        except TypeError:
            print('ff')
        #if iter(*args) != TypeError and iter({**kwargs}) != TypeError:
            #print("Все объекты итерируемые")
        result = fn(*args, **kwargs)
        return result

    return wrapper


@iter_arguments
def some_func(n, b, m, s):
    ...


if __name__ == "__main__":
    some_func(7, 8, m=8, s=9)
