from fastapi import FastAPI
from database import init_db
from tracker import get_transactions
from analyzer import detect_large_transactions

app = FastAPI(title="BlockPulse API")

init_db()


@app.get("/")
def root():
    return {"message": "BlockPulse is running"}


@app.get("/analyze/{wallet_address}")
def analyze_wallet(wallet_address: str):
    """
    Analyze wallet transactions and detect suspicious activity
    """
    transactions = get_transactions(wallet_address)
    suspicious = detect_large_transactions(transactions)

    return {
        "wallet": wallet_address,
        "suspicious_transactions": suspicious,
        "count": len(suspicious)
    }
