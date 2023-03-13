import sys


def decrypt(message: str):
    parts = message.partition('..')
    if parts[1] == '..':
        return decrypt(parts[0][:len(parts[0]) - 1] + parts[2])
    else:
        parts = message.partition('.')
        if parts[1] == '.':
            return decrypt(parts[0] + parts[2])
        else:
            return message


if __name__ == '__main__':
    message = sys.stdin.read()
    print(decrypt(message))
