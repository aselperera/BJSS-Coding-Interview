from main import lbtt_calculator

# Check values that fit in each bracket


def test_0():
    assert lbtt_calculator(0) == 0


def test_100():
    assert lbtt_calculator(100000) == 0


def test_200():
    assert lbtt_calculator(200000) == 1100


def test_300():
    assert lbtt_calculator(300000) == 4600


def test_400():
    assert lbtt_calculator(400000) == 13350


def test_800():
    assert lbtt_calculator(800000) == 54350

# Check very large value


def test_large():
    assert lbtt_calculator(500000000) == 59958350

# Check boundaries are implemented correctly


def test_145():
    assert lbtt_calculator(145000) == 0


def test_145_1():
    assert lbtt_calculator(145100) == 2


def test_250():
    assert lbtt_calculator(250000) == 2100


def test_251_1():
    assert lbtt_calculator(250100) == 2105


def test_325():
    assert lbtt_calculator(325000) == 5850


def test_325_1():
    assert lbtt_calculator(325100) == 5860


def test_750():
    assert lbtt_calculator(750000) == 48350


def test_750_1():
    assert lbtt_calculator(750100) == 48362
