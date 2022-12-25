def spirt(C, H, O):
    """ 
    функция получения целого числа малекул спирта
    из атомов углерода водорода и кислорода

    принимаемые значения
    С углерод
    Н водород 
    О кислород

    возвращает количество полученых малекул спирта
    """  
    try:
        C = int(C)
        H = int(H)
        O = int(O)
    except (TypeError, ValueError):
        return None

    C = round(int(C/2))   # количество углерода в спирте 2 
    H = round(int(H/6))   # количество водорода в спирте 6
    O = int(O)            # количество кислорода в спирте 1

    Spirt = [C, H, O]

    Spirt.sort()           # списком легче сортировать

    return Spirt[0]
