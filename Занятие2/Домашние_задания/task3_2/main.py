def positional_arguments(fn):
    def wrapper(*args):
        list_ = []
        for i in [*args]:
            if type(i) == int:
                list_.append(i)
        if [*args] == list_:
            print("Все аргументы функции являются типом int")
        result = fn(*args)
        return result

    return wrapper


@positional_arguments
def some_func(n, m, s):
    ...


if __name__ == "__main__":
    some_func(5, 6, 7)
