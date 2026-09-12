import requests

INDEXER_URL = "https://testnet-idx.algonode.cloud"

def verify_payment(txid, expected_receiver, min_amount):
    try:
        url = f"{INDEXER_URL}/v2/transactions/{txid}"

        response = requests.get(url)
        data = response.json()

        txn = data["transaction"]

        receiver = txn["payment-transaction"]["receiver"]
        amount_microalgos = txn["payment-transaction"]["amount"]

        amount_algos = amount_microalgos / 1_000_000

        if receiver == expected_receiver and amount_algos >= min_amount:
            return True

        return False

    except Exception as e:
        print("Verification error:", e)
        return False