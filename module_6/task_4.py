import itertools
import json
import collections


def counter_log_by_level(logs):
    for log_level, list_log in itertools.groupby(logs, key=lambda l: l['level']):
        print(f'{log_level}: {len(list(list_log))}')


def most_messages_in_an_hour(logs):
    hour_count_logs_dict = {}
    for hour, list_log in itertools.groupby(logs, key=lambda l: l['time'].split(':')[0]):
        hour_count_logs_dict[hour] = len(list(list_log))
    max_logs_by_hour = sorted(hour_count_logs_dict.items(), key=lambda item: item[1])[-1]
    print(f"Больше всего сообщений за следующий час - {max_logs_by_hour[0]}, сообщений - {max_logs_by_hour[1]}")


def count_critical_log_at_period(logs):
    result = [log for log in logs if log['level'] == 'CRITICAL' and '05:00:00' <= log['time'] <= '05:20:00']
    print(f'Количество логов CRITICAL с 05:00:00 по 05:20:00: {len(result)}')


def count_logs_by_dog_in_message(logs):
    result = [log for log in logs if 'dog' in log['message']]
    print(f"сообщений содержащих слово 'dog': {len(result)}")


def most_frequent_word_in_warning_log(logs):
    warning_log_message = [log['message'] for log in logs if log['level'] == 'WARNING']
    if len(warning_log_message) == 0:
        print("WARNING сообщения отсутствуют")
        return
    words = [word for word in [message.split() for message in warning_log_message]]
    most_frequent_word = collections.Counter(words).most_common()[0]
    print(f"Самое частое слово в WARNING сообщениях - {most_frequent_word[0]}, встречается{most_frequent_word[1]}")


if __name__ == '__main__':
    with open('skillbox_json_messages.log', 'r') as file_log:
        logs = [json.loads(log) for log in file_log.readlines()]

    counter_log_by_level(logs)
    most_messages_in_an_hour(logs)
    count_critical_log_at_period(logs)
    count_logs_by_dog_in_message(logs)
    most_frequent_word_in_warning_log(logs)
