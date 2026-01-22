from fastapi import FastAPI

app = FastAPI()

data = {
    "Chicken": 76,
    "Computer Science (Major)": 11,
    "Computer Science (Special)": 37,
    "Fish": 6,
    "Information Technology (Major)": 26,
    "Information Technology (Special)": 18,
    "Vegetable": 10
}


@app.get("/")
async def home():
    return data


@app.get("/stats")
async def stats():
    meal_preferences = {
        key: value
        for key, value in data.items()
        if key in ["Chicken", "Fish", "Vegetable"]
    }

    program_counts = {
        key: value
        for key, value in data.items()
        if key not in ["Chicken", "Fish", "Vegetable"]
    }

    return {
        "meal_preferences": meal_preferences,
        "program_counts": program_counts
    }


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": a + b
    }
    
