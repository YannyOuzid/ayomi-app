from utils.utils import compute, listToString, csvRowOrder

def test_compute():
    result = compute([4, 1, '+'])
    assert result == 5

def test_listToString():
    result = listToString([4, 1, '+'])
    assert result == '4 1 +'

def test_csvRowOrder():
    fixture = [
        {"equation": '4 1 +', "result": 5, "date": "2024-10-23"},
        {"equation": '4 2 +', "result": 6, "date": "2024-10-24"},
        {"equation": '4 3 +', "result": 7, "date": "2024-10-25"}
    ]
    result = csvRowOrder(fixture)
    assert result == [['4 1 +', 5, '2024-10-23'], ['4 2 +', 6, '2024-10-24'], ['4 3 +', 7, '2024-10-25']]