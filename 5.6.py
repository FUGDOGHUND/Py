import re

class Project:
    def __init__(self, fields1, fields2, source):
        self.fields1 = fields1
        self.fields2 = fields2
        self.source = source

    def __repr__(self):
        return f'Project({self.fields1}, {self.fields2}, {self.source})'

class Filter:
    def __init__(self, condition, source):
        self.condition = condition
        self.source = source

    def __repr__(self):
        return f'Filter({self.condition}, {self.source})'

class Eq:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Eq({self.left}, {self.right})'

class Field:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Field("{self.name}")'

class Value:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Value("{self.value}")'

class Scan:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return f'Scan("{self.filename}")'

def parse_sql(query):
    match = re.match(r"select (.*) from (.*\.csv) where (.*)='(.*)'", query)
    if match:
        fields = match.group(1).split(", ")
        filename = match.group(2)
        condition_field = match.group(3)
        condition_value = match.group(4)
        return Project(fields, fields, Filter(Eq(Field(condition_field), Value(condition_value)), Scan(filename)))

print(parse_sql("select room, title from talks.csv where time='09:00 AM'"))
