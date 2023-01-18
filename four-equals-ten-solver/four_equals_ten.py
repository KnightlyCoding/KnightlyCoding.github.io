from itertools import permutations as perm, combinations_with_replacement as cwr, combinations as com, product
    
def findeq(nums, o, par):
    paran = ([(-1, -1)] + list(cwr([0, 1, 2], 2))) if par else [(-1, -1)]
    if (0, 2) in paran:
        paran.remove((0, 2))
    for k in paran:
        for i in perm(nums):
            for j in product(o, repeat=3):
                eq = ['', str(i[0]), j[0], '', str(i[1]), '', j[1], '', str(i[2]), '', j[2], str(i[3]), '']
                if k[0] != -1:
                    eq[[0,3,7][k[0]]], eq[[5,9,12][k[1]]] = '(', ')'
                eq = ''.join(eq)
                try:
                    if eval(eq) == 10:
                        return eq
                except ArithmeticError:
                    pass
    return 'No answer'

def getAns(n1, n2, n3, n4):
    ao = ['+', '-', '*', '/'] if ((w:=input('Enter comma seperated list of available opperators (Enter for all): ')) == '') else w.split(',')
    p = True if input('Use parenthesis? (y/n): ') == 'y' else False
    print(findeq((n1, n2, n3, n4), ao, p))