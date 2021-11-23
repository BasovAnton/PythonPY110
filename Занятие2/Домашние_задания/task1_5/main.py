from string import ascii_lowercase, ascii_uppercase, digits
import random


def password_generator(n=8):
    dictionary = ascii_lowercase+ascii_uppercase+digits
    yield ''.join(random.sample(dictionary, n))


if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    for _ in range(10):
        print(next(password_generator(10)))
