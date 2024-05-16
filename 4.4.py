def group(parser):
    def parse_group(input, pos):
        result, pos_end = parser(input, pos)
        if result is None:
            return None, pos
        return (result,), pos_end
    return parse_group

def range_of(start, end):
    def parse_range(input, pos):
        if pos < len(input) and input[pos] >= start and input[pos] <= end:
            return input[pos], pos + 1
        return None, pos
    return parse_range

def alt(*parsers):
    def parse_alt(input, pos):
        for parser in parsers:
            result, pos_end = parser(input, pos)
            if result is not None:
                return result, pos_end
        return None, pos
    return parse_alt

def sym(char):
    def parse_sym(input, pos):
        if pos < len(input) and input[pos] == char:
            return char, pos + 1
        return None, pos
    return parse_sym

def seq(*parsers):
    def parse_seq(input, pos):
        results = []
        for parser in parsers:
            result, pos = parser(input, pos)
            if result is None:
                return None, pos
            results.append(result)
        return results, pos
    return parse_seq

def hex_colors(input, pos):
    digit = range_of('0', '9')
    hex_digit = alt(digit, range_of('a', 'f'), range_of('A', 'F'))
    space = alt(sym(' '), sym('\n'), sym('\t'))
    hex_color = seq(sym('#'), group(seq(hex_digit, hex_digit, hex_digit, hex_digit, hex_digit, hex_digit)))
    hex_colors_parser = seq(hex_color, sym(' '), hex_color)

    return hex_colors_parser(input, pos)

print(hex_colors('#ffaa43 #123456', 0))
