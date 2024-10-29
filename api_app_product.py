from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
print("Hello")

class NumberModel(BaseModel):
    num1: float
    num2: float
    num3: float

@app.post("/multiply")
async def multiply(num_model: NumberModel):
    """
    Multiply two numbers and return the result.

    Args:
        num_model (NumberModel): A dictionary containing two numbers to be multiplied.
            The keys should be 'num1' and 'num2'.

    Returns:
        float: The product of num1 and num2.
    """
    try:
        result = num_model.num1 * num_model.num2 * num_model.num3
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}