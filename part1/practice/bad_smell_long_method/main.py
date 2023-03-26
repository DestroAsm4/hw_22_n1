# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    # Чтение данных из строки
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data

def sort_by_age(data):
    # Сортировка по возрасту по возрастанию
    new_data = sorted(data, key=lambda x: x['age'])
    return new_data

def filter_age(data):
    # # Фильтрация
    result_data = list(filter(lambda k: k['age'] > 10, data))

    return result_data

def main():
    res = get_users_list()
    res = sort_by_age(res)
    res = filter_age(res)
    return res


if __name__ == '__main__':
    print(main())
