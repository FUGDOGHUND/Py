def range_of(start, end):
    def parse(text):
        if text and start <= text[0] <= end:
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


digit = range_of('0', '5')
number = seq(digit, digit)

print(number('42') is not None)
print(number('64') is not None)
