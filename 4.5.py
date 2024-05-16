def many(parser):
    def parse(text, results):
        remaining_text = text
        parsed_results = []

        while True:
            remaining_text, result = parser(remaining_text, results)
            if result is None:
                break
            parsed_results.append(result)

        return remaining_text, parsed_results

    return parse


def alt(*parsers):
    def parse(text, results):
        for parser in parsers:
            remaining_text, result = parser(text, results)
            if result is not None:
                return remaining_text, result
        return text, None

    return parse


def sym(character):
    def parse(text, results):
        if text and text[0] == character:
            return text[1:], character
        return text, None

    return parse


def range_of(start, end):
    def parse(text, results):
        if text and start <= text[0] <= end:
            return text[1:], text[0]
        return text, None

    return parse


def group(parser):
    def parse(text, results):
        remaining_text, result = parser(text, results)
        if result is not None:
            return remaining_text, [result]
        return text, None

    return parse


def seq(*parsers):
    def parse(text, results):
        remaining_text = text
        parsed_results = []

        for parser in parsers:
            remaining_text, result = parser(remaining_text, results)
            if result is None:
                return text, None
            parsed_results.extend(result)

        return remaining_text, parsed_results

    return parse


digit = range_of('0', '9')
hex_digit = alt(digit, range_of('a', 'f'), range_of('A', 'F'))
space = alt(sym(' '), sym('\n'), sym('\t'))
hex_color = seq(sym('#'), group(seq(hex_digit, hex_digit, hex_digit, hex_digit, hex_digit, hex_digit)))
hex_colors = many(seq(many(space), hex_color))


def parse_hex_colors(text, results):
    remaining_text, parsed_results = hex_colors(text, results)
    return remaining_text, [''.join(color[1]) for color in parsed_results if color[1]]


print(parse_hex_colors('''#ff10aa f3207a  bb1040 ABCD00''', []))
