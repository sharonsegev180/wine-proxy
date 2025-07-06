from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

SPOONACULAR_API_KEY = "1cb5906cd23447b395fb86df2f3c3428"

@app.get("/wine-pairing")
async def wine_pairing(food: str, maxPrice: float = None):
    base_url = "https://api.spoonacular.com/food/wine/pairing"
    params = {
        "food": food,
        "apiKey": SPOONACULAR_API_KEY
    }
    if maxPrice:
        params["maxPrice"] = maxPrice

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        return response.json()
