def sym(symbol):
    def parse(text):
        if text[0] == symbol:
            return text[1:]
        return None
    return parse

def seq(*parsers):
    def parse(text):
        for parser in parsers:
            text = parser(text)
            if text is None:
                return None
        return text
    return parse

# Пример использования комбинаторов
text = 'abc'
re1 = seq(sym('a'), sym('b'), sym('c'))
re2 = seq(sym('a'), sym('z'), sym('c'))
print(re1(text) is not None)
print(re2(text) is not None)
