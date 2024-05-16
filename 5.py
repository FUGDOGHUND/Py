import csv

def Scan(filename):
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yield row

print("Реализуйте генератор Scan('filename.csv'), который выдает очередную строку таблицы.")
for row in Scan('example_2.5kb.csv'):
    print(row)

print("\n")
def Print(parent):
    for row in parent:
        print(row)

print("Реализуйте функцию Print(parent), которая печатает все строки таблицы.")
Scan_generator = Scan('example_2.5kb.csv')
Print(Scan_generator)

print("\n")
print("Реализуйте генератор Filter(pred, filename), выдающий строки таблицы, для которых выполняется предикат pred. Для создания предикатов реализуйте ФВП Eq(x, y), Ne(x, y), Value(x), Field(x).")
def Eq(x, y):
    return lambda row: row[x] == y

def Ne(x, y):
    return lambda row: row[x] != y

def Value(x):
    return lambda row: row[x]

def Field(x):
    return x




def Filter(pred, filename):
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if pred(row):
                yield row


pred1 = Eq(0, 'Cordell Braun')



filtered_data1 = Filter(pred1, 'example_2.5kb.csv')



print("Filtered by name:")
Print(filtered_data1)



print("\nРеализуйте генератор Project(new_schema, parent_schema, parent), который выполняет операцию проекции.")

def Project(new_schema, parent_schema, parent):

    schema_mapping = {}
    for i, field in enumerate(parent_schema):
        if field in new_schema:
            schema_mapping[field] = i


    for row in parent:
        projected_row = [row[schema_mapping[field]] for field in new_schema]
        yield projected_row


parent_schema = ['Name', 'Age', 'City']
new_schema = ['Name', 'City']

parent_generator = Scan('example_2.5kb.csv')
projected_generator = Project(new_schema, parent_schema, parent_generator)


Print(projected_generator)
print("\nРеализуйте генератор Join(left, right), который выполняет операцию внутреннего соединения с помощью вложенных циклов.")

def Join(left, right):
    for left_row in left:
        for right_row in right:
            if left_row[0] == right_row[0]:
                yield left_row + right_row


left_schema = ['ID', 'Name']
right_schema = ['ID', 'City']

left_generator = Scan('example_2.5kb.csv')
right_generator = Scan('example_2.5kb.csv')

joined_generator = Join(left_generator, right_generator)


Print(joined_generator)

print("\nРеализуйте разбор SQL-подобного языка в разработанное представление на основе генераторов. Используйте в этой задаче комбинаторы регулярных выражений.")

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
