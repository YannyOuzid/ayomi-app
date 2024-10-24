from pydantic import BaseModel

class Calculator(BaseModel):
    equation: list
    date: str