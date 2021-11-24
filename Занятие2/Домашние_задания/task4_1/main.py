def get_distance(point: tuple):
    return ((point[1][0] - point[0][0]) ** 2 + (point[1][1] - point[0][1]) ** 2) ** 0.5


def task(points: list) -> list:
    return sum(list(map(get_distance, points)))


def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield [iterable[i], iterable[i + 1]]


def add_list(pts):
    list_ = []
    for pair in pairwise(pts):
        list_ += [pair]
    return list_


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    list_ = []
    for pair in pairwise(pts):
        list_ += [pair]

    print(task(list_))
