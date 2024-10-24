from utils.utils import compute, listToString, csvRowOrder

def individual_result(calculator) -> dict:
    return {
        "id": str(calculator["_id"]),
        "equation": calculator["equation"],
        "result": calculator["result"],
        "date": calculator["date"]
    }

def list_results(calculators) -> list:
    return[individual_result(calculator) for calculator in calculators]

def formatItem(item) -> object:
    result = compute(item.equation)
    request = {"equation": listToString(item.equation), "date": item.date, "result": result}
    return request