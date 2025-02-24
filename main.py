from stats import *


def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(contents)
    character_count = get_num_characters(contents)
    converted = convert_to_list_dict(character_count)
    sorted_list = converted.sort(reverse=True, key=sort_on)
    print(f"{num_words} words found in the document")
    print(sorted_list)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
