def count_set(int):
    set = 0
    while int:
        if int%2:
            set += 1
        int /= 2
    return set

def count_set_recur(int):
    if not int:
        return int
    else:
        return (int%2 + count_set_recur(int/2))

def count_set_bitwise(int):
    set = 0
    while int:
        if int & 1:
            set += 1
        int = int >> 1
    return set

def count_set_recur_bitwise(int):
    if not int:
        return int
    else:
        return ((int & 1) + count_set_recur(int >> 1))
