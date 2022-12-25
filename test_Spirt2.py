import Spirt2


def test_molecula_spirta_1():
    """ тест-функция 1 малекула из С=2 Н=6 О=1
    
    сравнивает количество получившихся целых малекул спирта
    с возвращаемым значением функции spirt
    """
    assert Spirt2.spirt(2, 6, 1) == 1

def test_molecula_spirta_2():
    """ тест-функция 2 малекула из С=45 Н=743 О=91
    
    сравнивает количество получившихся целых малекул спирта
    с возвращаемым значением функции spirt
    """
    assert Spirt2.spirt(45, 743, 91) == 22

def test_molecula_spirta_3():
    """ тест-функция на введение некорректных значений
    
    сравнивает количество получившихся целых малекул спирта
    с возвращаемым значением функции spirt
    """
    assert Spirt2.spirt('ds', 'fds', 'dfe') == None