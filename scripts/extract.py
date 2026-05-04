import requests
import os
from dotenv import load_dotenv
load_dotenv()

def getData():
    URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={os.getenv('APIKEY')}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    print(data)
    time_series = data.get("Time Series (Daily)", {})
    print(time_series)
    actions = []
    for date, values in time_series.items():
        action_date = {
            "date": date,
            "open": values.get("1. open"),
            "high": values.get("2. high"),
            "low": values.get("3. low"),
            "close": values.get("4. close"),
            "volume": values.get("5. volume")
        }
        actions.append(action_date)
    return actions

