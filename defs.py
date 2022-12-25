# написать еще пару функций
def add(x, y):
    """ функция сложения двух чисел
    
    принимает два параметра и возвращает сумму 
    """
    return x + y

def octatoc(x, y):
    """ функция остаток от деления
    
    делит аргумент x по модулю y
    """
    try:
        x = int(x)
        y = int(y)
    except (TypeError, ValueError):
        return print('Только целые числа')
    if y == 0:
        return print('на ноль делить нельзя')
    else:
        return x % y



print(octatoc('jdj', 6))
