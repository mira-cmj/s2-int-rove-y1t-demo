from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Rewards Redemption Optimizer API!"}

@app.get("/search")
def search_redemptions(origin: str, destination: str, date: str):
    # Placeholder logic for searching best-value redemptions
    return {"origin": origin, "destination": destination, "date": date, "results": []} 