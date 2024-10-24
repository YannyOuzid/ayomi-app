from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.calculators import Calculator
from config.database import collection
from schemas.schemas import list_results, formatItem
from bson import ObjectId
from utils.utils import csvRowOrder
import pandas as pd

router = APIRouter()

@router.get("/api/calculator")
async def get_results():
    """
    List of each item.
    Returns:
        A list of results
    """
    results = list_results(collection.find())
    return results

@router.post("/api/calculator")
async def post_result(calculator: Calculator):
    """
    Create one item.
    Returns:
        The body of the created item
    """
    request = formatItem(calculator)
    collection.insert_one(dict(request))
    return request

@router.delete("/api/calculator/{id}")
async def delete_result(id: str):
    """
    Remmove an item by ID.
    Args:
        id (_id): The ID of the item to delete.
    Returns:
        A string "Item deleted successfully"
    """
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return "Item deleted successfully"

@router.get("/api/calculator/csv")
async def get_csv():
    """
    Download the CSV of the item's list.
    Returns:
        A csv file
    """
    csvRow = list_results(collection.find())
    df = pd.DataFrame(
        csvRowOrder(csvRow), 
        columns=["Equation", "Result", "Date"]
    )
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"})