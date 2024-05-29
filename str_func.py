def all_caps():
    """Принимает на вход строку и возвращает ее со всеми заглавными буквами."""
    text = input().upper()
    print(text)


all_caps()

def first_caps(string):
    """Делает заглавными первые буквы каждого слова в строке, поступившей на вход."""
    words = string.split(" ")
    result = ""
    for word in words:
        word = word.capitalize()
        result += " " + word

    return result


string = input()
print(first_caps(string))