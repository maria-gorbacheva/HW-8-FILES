import os


def cook_book(txt_file):
    """
    function reads recipes from a text file, and builds a corresponding dictionary,
    which we can work with father
    :param txt_file: text file with each dish represented in format:
        Омлет
        3
        Яйцо | 2 | шт
        Молоко | 100 | мл
        Помидор | 2 | шт
     IMPORTANT: dishes must be separated with a blank string
    :return: dictionary cook_book{}
    """
    cook_book_dict = {}
    labels = ['ingredient_name', 'quantity', 'measure']
    file_path = os.path.join(os.getcwd(), txt_file)
    with open(file_path, encoding='utf-8-sig') as a:
        first_line = a.readline()
        while first_line:
            dish_name = first_line.strip()
            cook_book_dict[dish_name] = []
            num = int(a.readline())
            for i in range(num):
                parts = a.readline().strip().split(' | ')
                parts[1] = int(parts[1])
                cook_book_dict[dish_name].append(dict(zip(labels, parts)))
            a.readline()
            first_line = a.readline()
    return cook_book_dict


cook_book = cook_book('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for item in cook_book[dish]:
            if item['ingredient_name'] in result.keys():
                result[item['ingredient_name']]['quantity'] += item['quantity']
            else:
                result[item['ingredient_name']] = {'quantity': person_count * item['quantity'], 'measure': item['measure']}
    return result


print(cook_book)
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
