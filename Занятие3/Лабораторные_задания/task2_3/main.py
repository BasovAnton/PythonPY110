import json


def task():
    filename = "input.json"
    with open(filename) as f:
        python_object = json.load(f)

    return max(python_object, key=lambda i: i["score"])


if __name__ == "__main__":
    print(task())
