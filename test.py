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
    1: Question("Существует ли СССР?", 2, 0),
    2: Question("Является ли большинство Западной Африки частью Франции?", 3, 0),
    3: Question("Существует ли Пакистан?", 4, 0),
    4: Question("А Камбоджа?", 5, 0),
    5: Question("Объединённая Арабская Республика?", 6, 7),
    6: Answer("1958-1960."),
    7: Answer("1954-1957."),
    8: Question("Сущетвует ли Токио?", 9, 0),
    9: Question("Южная Африка?", 10, 0),
    10: Question("Австро-Венгрия?", 11, 0),
    11: Question("Албания?", 12, 13),
    12: Answer("1913-1918."),
    13: Answer("1910-1912."),
    14: Question("Гонк-Конг?", 15, 16),
    15: Answer("1992-1996."),
    16: Question("Сербия и серногория-одна страна?", 17, 0),
    17: Question("Восточный Тимор?", 18, 19),
    18: Answer("2002-2006."),
    19: Answer("1997-2001."),

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
