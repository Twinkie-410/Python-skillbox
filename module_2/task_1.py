def get_summary_rss(path: str, format):
    with open(path, 'r') as file:
        file_content = file.readlines()
        sum_rss = 0
        for line in file_content[1:]:
            sum_rss += int(line.split()[5])
    formats = {'B': 1/1024, 'KiB': 1, 'MiB': 1024, 'GiB': 1024 ** 2}
    if format in formats:
        return round(sum_rss / formats[format], 2)
    return 'неверный формат'


path_to_file = "/home/twinkie/Рабочий стол/output_file.txt"

if __name__ == '__main__':
    sum_rss = get_summary_rss(path_to_file, 'GiB')
    print(sum_rss)
