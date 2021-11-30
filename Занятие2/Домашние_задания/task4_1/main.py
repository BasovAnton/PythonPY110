from typing import Tuple


def get_distance(point: tuple) -> float:
    return ((point[1][0] - point[0][0]) ** 2 + (point[1][1] - point[0][1]) ** 2) ** 0.5


def task(points: list) -> float:
    point = new_list(points)
    return round(sum(list(map(get_distance, point))), 2)


def pairwise(iterable: list): #-> Tuple[(float, float), (float, float)]
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


def new_list(points: list) -> list:
    list_ = []
    for pair in pairwise(points):
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
