def get_num_words(book_contents):
    words = book_contents.split()
    num_words = len(words)
    return num_words


def get_num_characters(book_contents):
    lowered_contents = book_contents.lower()

    characters = {}

    for char in lowered_contents:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters


def sort_on(dic):
    new_dict = dict(sorted(dic.items(), key=lambda item: item[::-1]))
    return new_dict
