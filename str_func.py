def str_func(line):
    """принимает на вход строку и возвращает
    ее со всеми заглавными Буквами"""
    return line.upper()


def str_func_2(line):
    """делает заглавными первые буквы каждого
    слова в строке, поступившей на вход"""
    final_line = []
    for i in line.split(' '):
        final_line.append(i.capitalize())
    return ' '.join(final_line)
