import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = ####\s(?P<position>\d{1,2})\.\s\[(?P<book>.+)\]\((?P<book_url>https.+?)\).by.(?P<author>.+)\s\((?P<recommended>\d+.\d+%).+\s!\[\](?P<cover_url>\(https:.+\))\s+(?P<description>\".+\.\")


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
