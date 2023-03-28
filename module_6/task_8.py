phone_keys = {'2': 'abc',
              '3': 'def',
              '4': 'ghi',
              '5': 'jkl',
              '6': 'mno',
              '7': 'pqrs',
              '8': 'tuv',
              '9': 'wxyz'}


def my_t9(input_numbers: str):
    with open('words.txt', 'r') as file:
        words = file.read().split('\n')

    filtered_words_by_len = tuple(filter(lambda word: len(word) == len(input_numbers), words))
    result = []
    for word in filtered_words_by_len:
        word_corresponds = True
        for index, letter in enumerate(word):
            if letter not in phone_keys[input_numbers[index]]:
                word_corresponds = False
                break
        if word_corresponds:
            result.append(word)
    return result


if __name__ == '__main__':
    print(*my_t9('22736368'))
