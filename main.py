from stats import *
import sys


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        contents = get_book_text(sys.argv[1])
        num_words = get_num_words(contents)
        character_count = get_num_characters(contents)
        converted = convert_to_list_dict(character_count)
        converted.sort(reverse=True, key=sort_on)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        make_pretty(converted)
        print("============= END ===============")


def make_pretty(list_dicts):
    for dict in list_dicts:
        char = next(iter(dict.keys()))
        count = next(iter(dict.values()))
        print(f"{char}: {count}")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
