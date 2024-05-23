import csv

def Scan(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # пропустить заголовок
        for row in reader:
            yield row

def Print(parent):
    for row in parent:
        print(row)

def Eq(x, y):
    return x == y

def Ne(x, y):
    return x != y

def Value(x):
    return x

def Field(x):
    return x

def Filter(pred, generator):
    for row in generator:  # Используем прямое итерирование по генератору
        if pred(row):
            yield row

def Project(new_schema, parent_schema, parent):
    indices = [parent_schema.index(col) if col in parent_schema else -1 for col in new_schema]
    for row in parent:
        yield [row[i] if i != -1 else '' for i in indices]

def Join(left, right):
    for row1 in left:
        for row2 in right:
            yield row1 + row2

# Пример использования
result = Project(['room', 'title'], ['room', 'title'],
                  Filter(lambda row: Eq(row[1], '09:00 AM'), Scan('talks.csv')))

for row in result:
    print(row)

result = Filter(lambda row: Ne(row[2], row[3]),
                Join(
                  Project(['time', 'room', 'title1'], ['time', 'room', 'title'],
                          Scan('talks.csv')),
                  Project(['time', 'room', 'title2'], ['time', 'room', 'title'],
                          Scan('talks.csv'))
                      )
                )

for row in result:
    print(row)