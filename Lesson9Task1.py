# Task 1
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

def is_arithmetic_sequence(x):
    if len(x) < 2:
        return False
    d = x[1] - x[0]
    for i in range(len(x) - 1):
        if x[i + 1] - x[i] != d:
            return False
    return True


def is_geometric_sequence(x):
    if len(x) < 2:
        return False
    if not x[0]:
        return False
    q = x[1] // x[0]
    for i in range(len(x) - 1):
        if x[i + 1] // x[i] != q:
            return False
    return True


def next_arithmetic_sequence(x):
    d = x[1] - x[0]
    return x[-1] + d


def next_geometric_sequence(x):
    q = x[1] // x[0]
    return x[-1] * q


def main():
    seq = input('items=').replace(' ', '')
    seq = seq.split(',')
    seq = list(map(int, seq))

    if is_arithmetic_sequence(seq):
        print(next_arithmetic_sequence(seq))
    elif is_geometric_sequence(seq):
        print(next_geometric_sequence(seq))
    else:
        print('Not defined')


if __name__ == '__main__':
    main()