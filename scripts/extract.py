import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def getData():
    API_KEY = os.getenv("APIKEY")
    SYMBOL = "IBM"

    URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"Erro na API: {data}")

    time_series = data.get("Time Series (Daily)", {})

    actions = []
    for date, values in time_series.items():
        action_date = {
            "symbol": SYMBOL,
            "date": date,
            "open": float(values.get("1. open")),
            "high": float(values.get("2. high")),
            "low": float(values.get("3. low")),
            "close": float(values.get("4. close")),
            "volume": int(values.get("5. volume"))
        }
        actions.append(action_date)
    return actions

if __name__ == "__main__":
    actions = getData()

    with open("../database/actions.json", "w") as outfile:
        json.dump(actions, outfile, indent=4)

    print("\33[32m Dados extraídos e salvos com sucesso! \33[m")

