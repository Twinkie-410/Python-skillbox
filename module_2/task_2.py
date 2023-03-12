import sys


def get_mean_size(input):
    lines = input.split('\n')[1:-1]
    count = len(lines)
    if count == 0:
        return 'нет файлов'
    sum_size = 0
    for line in lines:
        size = line.split()[4]
        if size == '':
            return f'не удалось получить размер файла {line.split()[-1]}'
        sum_size += int(size)
    return sum_size/count


if __name__ == '__main__':
    data = sys.stdin.read()
    print(get_mean_size(data))
