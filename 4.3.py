def alt(*parsers):
    def parse(text):
        for parser in parsers:
            result = parser(text)
            if result is not None:
                return result
        return None
    return parse

def range_of(start, end):
    def parse(text):
        if text and start <= text[0] <= end:
            return text[1:]
        return None
    return parse

def sym(char):
    def parse(text):
        if text and text[0] == char:
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
digit = range_of('0', '9')
hex_digit = alt(digit, range_of('a', 'f'), range_of('A', 'F'))
space = alt(sym(' '), sym('\n'), sym('\t'))
hex_color = seq(sym('#'), hex_digit, hex_digit, hex_digit, hex_digit, hex_digit, hex_digit)

print(hex_color('#ffaa43') is not None)  # True
print(hex_color('#xxxxxx') is not None)  # False
