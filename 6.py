
print("Реализуйте интерпретатор нормальных алгоритмов Маркова (НАМ). Обойдитесь без поддержки завершающих правил (стрелка с точкой).")
def markov(input_str, rules):
    while True:
        applied_rule = False
        for rule in rules:
            pattern, replacement = rule
            if pattern in input_str:
                input_str = input_str.replace(pattern, replacement, 1)
                applied_rule = True
                break
        if not applied_rule:
            break
    return input_str

rules = [
    ('|0', '0||'),
    ('1', '0|'),
    ('0', '')
]

print(markov('111', rules))



rules = [
    ('parity(0)', 'even'),
    ('parity(1)', 'odd'),
    ('parity(10)', 'even'),
    ('parity(11)', 'odd'),
    ('parity(00)', 'even'),
    ('parity(01)', 'odd'),
    ('parity()', ''),  # если нет числа, то оно четное
    ('parity(even)', 'even'),  #  как четное
    ('parity(odd)', 'odd')  #  как нечетное
]

def markov(input_str, rules):
    while True:
        applied_rule = False
        for pattern, replacement in rules:
            if pattern in input_str:
                input_str = input_str.replace(pattern, replacement, 1)
                applied_rule = True
                break
        if not applied_rule:
            break
    return input_str
print("Релизуйте НАМ для проверки четности двоичного числа. Пример работы:")

print(markov('parity(110)', rules))
print(markov('parity(1010010)', rules))


print("Реализуйте НАМ для проверки арифметического выражения на корректный синтаксис. Пример работы:")
import re

def markov(expression, rules):

    result = ''
    for char in expression:
        if char in rules:
            result += rules[char]
        else:
            result += char
    return result


rules = {
    '+': 'E',
    '-': 'E',
    '*': 'E',
    '/': 'E',
    '(': '(',
    ')': ')',
    ' ': ''
}


print(markov(' (123 /3) ', rules))
print(markov(' -12 ', rules))


print("Марков 2.0")
class Term:
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __repr__(self):
        if self.args:
            return f"{self.name}({', '.join(map(str, self.args))})"
        return self.name

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.name == other.name and self.args == other.args
        return False

def match(term, pattern):
    if isinstance(pattern, str) and pattern.startswith('$'):
        return {pattern: term}
    if isinstance(term, Term) and isinstance(pattern, Term):
        if term.name != pattern.name or len(term.args) != len(pattern.args):
            return None
        substitutions = {}
        for t, p in zip(term.args, pattern.args):
            sub = match(t, p)
            if sub is None:
                return None
            for k, v in sub.items():
                if k in substitutions and substitutions[k] != v:
                    return None
                substitutions[k] = v
        return substitutions
    if term == pattern:
        return {}
    return None

def substitute(term, substitutions):
    if isinstance(term, str) and term.startswith('$'):
        return substitutions.get(term, term)
    if isinstance(term, Term):
        return Term(term.name, *[substitute(arg, substitutions) for arg in term.args])
    return term

def apply_rule(term, rule):
    pattern, replacement = rule
    substitutions = match(term, pattern)
    if substitutions is not None:
        return substitute(replacement, substitutions)
    return None

def rewrite(term, rules):
    for rule in rules:
        new_term = apply_rule(term, rule)
        if new_term is not None:
            return new_term
    if isinstance(term, Term):
        new_args = [rewrite(arg, rules) for arg in term.args]
        if new_args != term.args:
            return Term(term.name, *new_args)
    return term

def full_rewrite(term, rules):
    while True:
        new_term = rewrite(term, rules)
        if new_term == term:
            return term
        term = new_term

# Примеры правил
rules = [
    (Term('f', Term('$x'), Term('g', Term('$y'), Term('$z'))), Term('h', Term('$x'), Term('$y'), Term('$z'))),
    (Term('add', Term('$x'), Term('0')), Term('$x')),
    (Term('add', Term('$x'), Term('succ', Term('$y'))), Term('succ', Term('add', Term('$x'), Term('$y'))))
]

# Примеры использования

term1 = Term('f', 'a', Term('g', 'b', 'c'))
result1 = full_rewrite(term1, rules)
print(f"Rewrite {term1} -> {result1}")


term2 = Term('add', Term('succ', Term('succ', '0')), Term('succ', '0'))
result2 = full_rewrite(term2, rules)
print(f"Rewrite {term2} -> {result2}")
