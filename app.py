from fastapi import FastAPI
from algorand_verify import verify_payment

app = FastAPI()

PAID = False


@app.get("/")
def home():
    return {
        "project": "Scale-Adaptive Hybrid Matcher",
        "status": "running"
    }


@app.get("/analyze-images")
def analyze_images():

    # Mock outputs for now
    scale_ratio = 12.4
    viewpoint_variation = "high"
    illumination_change = "medium"
    geometric_variation = "high"

    complexity_score = 78

    premium_required = complexity_score >= 50

    return {
        "scale_ratio": scale_ratio,
        "viewpoint_variation": viewpoint_variation,
        "illumination_change": illumination_change,
        "geometric_variation": geometric_variation,
        "complexity_score": complexity_score,
        "premium_required": premium_required
    }


@app.get("/register-basic")
def register_basic():

    return {
        "tier": "basic",
        "algorithm": "AKAZE",
        "matches": 82,
        "status": "Registration Complete"
    }


@app.get("/register-pro")
def register_pro():

    if not PAID:
        return {
            "error": "Premium Payment Required"
        }

    return {
        "tier": "premium",
        "algorithm": "SAHM",
        "matches": 154,
        "rmse": 0.89,
        "status": "Registration Complete"
    }


TEAM_WALLET = "PHF64DR2Y2BBVC56EORSYFUYU7Y7I4CLB22HHLUKP3QKYAZIBQ3IXZ3MBU"

@app.get("/pay")
def pay():

    return {
        "message": "Send payment",
        "receiver": TEAM_WALLET,
        "amount": 0.1,
        "network": "Algorand TestNet"
    }


@app.get("/reset")
def reset():

    global PAID
    PAID = False

    return {
        "message": "Payment Status Reset"
    }
    
@app.get("/verify-payment")
def verify(txid: str):

    global PAID

    valid = verify_payment(
        txid,
        TEAM_WALLET,
        0.1
    )

    if valid:
        PAID = True
        return {
            "verified": True
        }

    return {
        "verified": False
    }