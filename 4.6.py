def parse(text, pattern):

    result = pattern(text)
    if result is not None:
        remainder, match = result
        return [match] + parse(remainder, pattern) if remainder else [match]
    return []

def digit(text):

    if text and text[0].isdigit():
        return text[1:], text[0]
    return None

def many(pattern):

    def many_pattern(text):
        matches = []
        while True:
            result = pattern(text)
            if result is None:
                break
            text, match = result
            matches.append(match)
        return text, matches
    return many_pattern

def seq(*patterns):

    def seq_pattern(text):
        matches = []
        for pattern in patterns:
            result = pattern(text)
            if result is None:
                return None
            text, match = result
            matches.append(match)
        return text, matches
    return seq_pattern

def findall(pattern):

    def findall_pattern(text, matches):
        result = pattern(text)
        if result is None:
            return text, matches
        remainder, match = result
        return findall_pattern(remainder, matches + [match])
    return findall_pattern


text = '12dasd dsa82 a-'
num = seq(digit, many(digit))
print(findall(num)(text, []))
#Реализуйте комбинатор findall (найти все фрагменты по шаблону).
