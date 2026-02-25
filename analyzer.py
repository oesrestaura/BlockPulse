def detect_large_transactions(transactions, threshold_eth=10):
    """
    Detect transactions larger than threshold (in ETH)
    """
    suspicious = []

    for tx in transactions:
        # Convert Wei to ETH
        value_eth = int(tx["value"]) / 10**18

        if value_eth >= threshold_eth:
            suspicious.append({
                "hash": tx["hash"],
                "from": tx["from"],
                "to": tx["to"],
                "value_eth": value_eth
            })

    return suspicious
