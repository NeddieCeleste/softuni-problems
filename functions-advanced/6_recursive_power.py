from functools import reduce

def sum_nums(*args):
    return sum(args)

def sub_numbs(*args):
    return reduce(lambda x, y: x-y, args)

def mul_nums(*args):
    return reduce(lambda x, y: x*y, args)

def div_nums(*args):
    return reduce(lambda x, y: x/y, args)

mapper = {
    "+": sum_nums,
    "-": sub_numbs,
    "*": mul_nums,
    "/": div_nums,
}

def operate(sign, *args):
    func = mapper[sign]
    return func(*args)