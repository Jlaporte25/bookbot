from stats import get_num_words, get_num_characters, sort_dict


def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(contents)
    character_count = get_num_characters(contents)
    sorted_count = sort_dict(character_count)
    print(f"{num_words} words found in the document")
    print(sorted_count)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
