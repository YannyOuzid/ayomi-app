from collections import deque
 
def compute(sequence: list) -> float:
    d = deque()
    for touche in sequence:
        if isinstance(touche, int):
            d.append(touche)
        elif isinstance(touche, str):
            b, a = d.pop(), d.pop()
            expr = f"{a} {touche} {b}"
            d.append(eval(expr))
        else:
            raise ValueError(f"Expression invalide: {touche}")
        print(f"{d}  # {touche}")
    return d.pop()

def listToString(list: list) -> str:
    return ' '.join(str(e) for e in list)

def csvRowOrder(list: list) -> list:
    csvRows = []
    for x in list:
        csvRows.append([x["equation"], x["result"], x["date"]])
    return csvRows
