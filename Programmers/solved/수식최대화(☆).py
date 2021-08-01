# def split_expression(expression):
#     exp, tmp = list(), str()
#     for e in expression:
#         if e.isdigit():
#             tmp += str(e)
#         else:
#             exp.append(tmp)
#             exp.append(e)
#             tmp = ''
#     exp.append(tmp)

#     for i, e in enumerate(exp):
#         if e not in ['*','+','-']:
#             exp[i] = int(e)

#     return exp

# def calc_multiple(expr):
#     while True:
#         if '*' not in expr:
#             break

#         else:
#             idx = expr.index('*')
#             front_num = expr[idx-1]
#             rear_num = expr[idx+1]
#             result_num = front_num * rear_num
#             del expr[idx-1]
#             del expr[idx-1]
#             expr[idx-1] = result_num

#     return expr

# def calc_plus(expr):
#     while True:
#         if '+' not in expr:
#             break

#         else:
#             idx = expr.index('+')
#             front_num = expr[idx-1]
#             rear_num = expr[idx+1]
#             result_num = front_num + rear_num
#             del expr[idx-1]
#             del expr[idx-1]
#             expr[idx-1] = result_num
            
#     return expr

# def calc_minus(expr):
#     while True:
#         if '-' not in expr:
#             break

#         else:
#             idx = expr.index('-')
#             front_num = expr[idx-1]
#             rear_num = expr[idx+1]
#             result_num = front_num - rear_num
#             del expr[idx-1]
#             del expr[idx-1]
#             expr[idx-1] = result_num
            
#     return expr


# def solution(expression):
#     answer = []
#     origin_expr = split_expression(expression)

#     # * > + > -
#     expr = origin_expr.copy()
#     expr = calc_multiple(expr)
#     expr = calc_plus(expr)
#     expr = calc_minus(expr)
#     answer.append(abs(expr[0]))

#     # * > - > +
#     expr = origin_expr.copy()
#     expr = calc_multiple(expr)
#     expr = calc_minus(expr)
#     expr = calc_plus(expr)
#     answer.append(abs(expr[0]))

#     # + > * > -
#     expr = origin_expr.copy()
#     expr = calc_plus(expr)
#     expr = calc_multiple(expr)    
#     expr = calc_minus(expr)
#     answer.append(abs(expr[0]))

#     # + > - > *
#     expr = origin_expr.copy()
#     expr = calc_plus(expr)
#     expr = calc_minus(expr)
#     expr = calc_multiple(expr)
#     answer.append(abs(expr[0]))

#     # - > * > +
#     expr = origin_expr.copy()
#     expr = calc_minus(expr)
#     expr = calc_multiple(expr)
#     expr = calc_plus(expr)
#     answer.append(abs(expr[0]))

#     # - > + > *
#     expr = origin_expr.copy()
#     expr = calc_minus(expr)
#     expr = calc_plus(expr)
#     expr = calc_multiple(expr)
#     answer.append(abs(expr[0]))

#     return max(answer)


import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    print("op = ", op)
    op = [list(y) for y in permutations(op)]
    print("op = ", op)
    ex = re.split(r'(\D)',expression)
    print("ex = ", ex)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])
    print(a)
    
    #3
    return max(abs(int(x)) for x in a)

expression = "50*6-3*2"
s = solution(expression)
print(s)