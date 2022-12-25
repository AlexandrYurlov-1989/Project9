import defs


def test_add_1():
    assert defs.add(3, 5) == 8

def test_add_2():
    assert defs.add(5, 5) == 10

def test_add_3():
    assert defs.add(0, 0) == 0

def test_add_4():
    assert defs.add(0.5, 0.5) == 1

def test_add_5():
    assert defs.add(-1, -1) == -2

def test_octatoc_1():
    assert defs.octatoc(1, 1) == 0

def test_octatoc_2():
    assert defs.octatoc(-1, -1) == 0

def test_octatoc_3():
    assert defs.octatoc(0.5, 0.5) == None

def test_octatoc_4():
    assert defs.octatoc(4, 3) == 1

def test_octatoc_5():
    assert defs.octatoc(15, 7) == 1

def test_octatoc_6():
    assert defs.octatoc(983, 461) == 61

def test_octatoc_6():
    assert defs.octatoc(983, 461) == 61

def test_octatoc_7():
    assert defs.octatoc(-1, -2) == -1

def test_octatoc_8():
    assert defs.octatoc(-1, 2) == 1

def test_octatoc_9():
    assert defs.octatoc(-0.78, -0.35) == None

def test_octatoc_10():
    assert defs.octatoc(2, 0) == None

def test_octatoc_11():
    assert defs.octatoc('jjhd', 0) == None

