from schemas.schemas import individual_result, list_results, formatItem
from models.calculators import Calculator

def test_individual_results():
    result = individual_result({"_id": '1', "equation": '4 1 +', "result": 5, "date": "2024-10-23"})
    assert result == {"id": '1', "equation": '4 1 +', "result": 5, "date": "2024-10-23"}

def test_list_results():
    fixture = [
        {"_id": '1', "equation": '4 1 +', "result": 5, "date": "2024-10-23"},
        {"_id": '2', "equation": '4 2 +', "result": 6, "date": "2024-10-24"},
        {"_id": '3', "equation": '4 3 +', "result": 7, "date": "2024-10-25"}
    ]

    shouldLooksLike = [
        {"id": '1', "equation": '4 1 +', "result": 5, "date": "2024-10-23"},
        {"id": '2', "equation": '4 2 +', "result": 6, "date": "2024-10-24"},
        {"id": '3', "equation": '4 3 +', "result": 7, "date": "2024-10-25"}
    ]
    result = list_results(fixture)
    assert result == shouldLooksLike

def test_formatItem():
    item = Calculator(equation = [4, 1, '+'], date = "2024-10-23")
    result = formatItem(item)
    assert result == {"equation": '4 1 +', "result": 5, "date": "2024-10-23"}