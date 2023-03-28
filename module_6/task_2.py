import re


def is_strong_password(password):
    with open('words.txt', 'r') as file:
        words_file = file.read()
        words = re.findall('[a-z]+', words_file, flags=re.IGNORECASE)
        for word in words:
            if len(word) > 3 and word in password.lower():
                return False
        return True


print(is_strong_password('$mfKeBirdfn32_vjerf')) #False
