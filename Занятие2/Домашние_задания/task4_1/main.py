def get_distance(point: tuple):
    return ((point[1][0] - point[0][0]) ** 2 + (point[1][1] - point[0][1]) ** 2) ** 0.5


def task(points) -> list:
    point = new_list(points)
    return sum(list(map(get_distance, point)))


def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield [iterable[i], iterable[i + 1]]


def new_list(lt):
    list_ = []
    for pair in pairwise(lt):
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

    print(task(pts))
