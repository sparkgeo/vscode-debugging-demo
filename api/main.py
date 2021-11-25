from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/valid")
async def valid():
    response = requests.get('https://api.github.com')
    response.raise_for_status()
    return response.json()


@app.get("/invalid")
async def invalid():
    response = requests.get('https://api.github.com/invalid')
    response.raise_for_status()
    return response.json()
