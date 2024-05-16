from typing import NamedTuple, Union
class Num:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value

class Add:
    def __init__(self, *args):
        self.operands = args[0] if len(args) == 1 else args
        self.value = sum(op.value for op in self.operands)

class Mul:
    def __init__(self, *args):
        self.operands = args[0] if len(args) == 1 else args
        self.value = 1
        for op in self.operands:
            self.value *= op.value

Expr = Union[Num, Add, Mul]

#Реализуйте PrintVisitor в виде функции print_expr.

def print_expr(expr: Expr) -> str:
    if isinstance(expr, Num):
        return str(expr.value)
    elif isinstance(expr, Add):
        return '(' + ' + '.join(print_expr(op) for op in expr.operands) + ')'
    elif isinstance(expr, Mul):
        return '(' + ' * '.join(print_expr(op) for op in expr.operands) + ')'
    else:
        raise ValueError("Unexpected expression type")

#Реализуйте CalcVisitor в виде функции calc_expr.
def calc_expr(expr: Expr) -> int:
    if isinstance(expr, Num):
        return expr.value
    elif isinstance(expr, Add):
        return sum(calc_expr(op) for op in expr.operands)
    elif isinstance(expr, Mul):
        total = 1
        for op in expr.operands:
            total *= calc_expr(op)
        return total
    else:
        raise ValueError("Unexpected expression type")
#Реализуйте StackVisitor в виде функции stack_expr.
def stack_expr(expr: Expr) -> str:
    if isinstance(expr, Num):
        return f"PUSH {expr.value}\n"
    elif isinstance(expr, Add):
        return ''.join(stack_expr(op) for op in expr.operands) + "ADD\n"
    elif isinstance(expr, Mul):
        return ''.join(stack_expr(op) for op in expr.operands) + "MUL\n"
    else:
        raise ValueError("Unexpected expression type")

#Реализуйте функцию dot_expr для печати дерева выражения на языке Graphviz.
def dot_expr(expr: Expr) -> str:
    def generate_dot(node, node_id):
        nonlocal dot_representation, next_node_id
        if isinstance(node, Num):
            dot_representation += f"n{node_id} [label=\"{node.value}\" shape=circle]\n"
        elif isinstance(node, Add):
            dot_representation += f"n{node_id} [label=\"+\" shape=circle]\n"
        elif isinstance(node, Mul):
            dot_representation += f"n{node_id} [label=\"*\" shape=circle]\n"

        if isinstance(node, (Add, Mul)):
            for operand in node.operands:
                next_node_id += 1
                dot_representation += f"n{node_id} -> n{next_node_id}\n"
                generate_dot(operand, next_node_id)

    dot_representation = "digraph G {\n"
    next_node_id = 0
    generate_dot(expr, next_node_id)
    dot_representation += "}\n"
    return dot_representation




if __name__ == "__main__":
    if __name__ == "__main__":
        ast = Add(Num(7), Mul(Num(3), Num(2)))
        print("Expression:", print_expr(ast))
        print("Result:", calc_expr(ast))
        print("Stack representation:")
        print(stack_expr(ast))
        print("Graphviz representation:")
        print(dot_expr(ast))

