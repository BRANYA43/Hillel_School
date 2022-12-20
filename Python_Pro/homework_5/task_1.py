WORD = 0
VALUE = 1
LAST_FREQUENTLY_WORD = -1


def get_frequently_word(text: str) -> str:
    words = text.split()
    word_counts = {}

    for word in words:
        if word_counts.get(word) is None:
            word_counts.setdefault(word, 0)
        word_counts[word] += 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda kv: kv[VALUE])
    return sorted_word_counts[LAST_FREQUENTLY_WORD][WORD]


if __name__ == '__main__':
    text_ = input('Input text: ')
    print(get_frequently_word(text_))
