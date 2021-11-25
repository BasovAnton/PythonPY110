def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


pts = [
    (3, 4),
    (4.5, 3),
    (2.1, -1),
    (6.8, -3),
    (1.4, 2.9)
]


def get_distance(point: tuple):
    return ((point[1][0] - point[0][0]) ** 2 + (point[1][1] - point[0][1]) ** 2) ** 0.5

x = []
for pair in pairwise(pts):
    x += [pair]

print(x)

if __name__ == "__main__":
    kwargs = {1: 2, 2: 3, 4: 5}
    x = map(lambda  key: (key, kwargs[key]), kwargs)
    print(next(x))
    print(next(x))

