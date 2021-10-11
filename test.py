class Question:
    def __init__(self, question, true, false):
        self.question = question
        self.true = true
        self.false = false


class Answer:
    def __init__(self, answer):
        self.answer = answer


nodes = {
    0: Question("Есть ли на карте Стамбул?", 1, 8),
    1: Question("Существует ли СССР?", 2, 14),
    2: Question("Является ли большинство Западной Африки частью Франции?", 3, 23),
    3: Question("Существует ли Пакистан?", 4, 28),
    4: Question("А Камбоджа?", 5, 31),
    5: Question("Объединённая Арабская Республика?", 6, 7),
    6: Answer("1958-1960."),
    7: Answer("1954-1957."),
    8: Question("Сущетвует ли Токио?", 9, 0),
    9: Question("Южная Африка?", 10, 35),
    10: Question("Австро-Венгрия?", 11, 42),
    11: Question("Албания?", 12, 13),
    12: Answer("1913-1918."),
    13: Answer("1910-1912."),
    14: Question("Гонк-Конг?", 15, 16),
    15: Answer("1992-1996."),
    16: Question("Сербия и серногория-одна страна?", 17, 20),
    17: Question("Восточный Тимор?", 18, 19),
    18: Answer("2002-2006."),
    19: Answer("1997-2001."),
    20: Question("Южный Судан?",21,22),
    21: Answer("2007-2011"),
    22: Answer("2011-2014"),
    23: Question("Вьетнам один?",24,25),
    24: Answer("1979-1981"),
    25: Question("Бангладеш существует?",26,27),
    26: Answer("1972-1975"),
    27: Answer("1969-1971"),
    28: Question("Германия одна?",29,0),
    29: Answer("1940-1945"),
    30: Answer("1946-1947"),
    31: Question("Эритерия-часть Италии?",32,45),
    32: Question("Канаде не хватает кусочка?",33,34),
    33: Answer("1948"),
    34: Answer("1948-1952"),
    35: Question("Существует ли Родезия?",36,39),
    36: Question("Норвегия часть Швеции?",37,38),
    37: Answer("1896-1905"),
    38: Answer("1906-1909"),
    39: Question("Боливия не имеет выхода к морю?",40,41),
    40: Answer("1884-1895"),
    41: Answer("1872-1883"),
    42: Question("Существует ли Ленинград?",43,44),
    43: Answer("1924-1929"),
    44: Answer("1919-1923"),
    45: Answer("1952-1953")


}


def eval(node):
    if(isinstance(node, Answer)):
        send_message(node.answer)
        return
    answer = ask_user(node.question)
    if(answer == 'y'):
        eval(nodes[node.true])
    else:
        eval(nodes[node.false])


def ask_user(text):
    print(text)
    answer = input()
    return answer


def send_message(text):
    print(text)


if __name__ == '__main__':
    eval(nodes[0])
