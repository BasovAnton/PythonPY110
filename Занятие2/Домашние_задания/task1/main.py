from itertools import count

if __name__ == "__main__":
    q = 3
    elem = (q**i for i in count(1, 1))

    for i in range(1, 20):
        print(next(elem))
