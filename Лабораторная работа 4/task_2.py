def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()

    for i in str_:
        if i.isalpha() and i in dict_:
            dict_[i] += 1
        elif i.isalpha() and i not in dict_:
            dict_[i] = 1
        else:
            pass
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
x = get_count_char(main_str).copy()

def new_dict_(dict_char):
    sum_value = sum(dict_char.values())    
    for key, value in dict_char.items():
        dict_char[key] = round(value / sum_value * 100, 1)
    return dict_char

print(new_dict_(x))
