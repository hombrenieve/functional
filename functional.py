def fin(n):
    return n % 10


def pri(n):
    if n < 10:
        return n
    else:
        return pri(n / 10)


def cif(n):
    if n < 10:
        return 1
    else:
        return 1 + cif(n / 10)


def pow(b, e):
    if e == 0:
        return 1
    else:
        return b * pow(b, e - 1)


def inv(n):
    if n < 10:
        return n
    else:
        return (n % 10) * pow(10, cif(n) - 1) + inv(n / 10)


def med(n):
    return inv(inv(n) / 10) / 10


def capicua(n):
    if n < 10:
        return True
    else:
        return pri(n) == fin(n) and capicua(med(n))


def buscar(n, l):
    if len(l) == 0:
        return False
    return n == l[0] or buscar(n, l[1:])


def sum(l):
    if len(l) == 0:
        return 0
    return l[0] + sum(l[1:])


def sumPar(l):
    if len(l) < 2:
        return []
    if len(l) == 2:
        return [l[0] + l[1]]
    return [l[0] + l[1]] + sumPar(l[1:])


def concat(l, ll):
    if len(l) == 0:
        return ll
    return [l[0]] + concat(l[1:], ll)


def interlace(el, ll):
    if len(ll) == 0:
        return []
    return concat(inter2(el, ll[0]), interlace(el, ll[1:]))


def perm(l):
    if len(l) == 0:
        return []
    return interlace(l[0], l[1:])


def tartlev(n):
    if n == 1:
        return [1]
    return [1] + sumPar(tartlev(n - 1)) + [1]


def tart(n):
    if n == 1:
        return [[1]]
    return tart(n - 1) + [tartlev(n)]
