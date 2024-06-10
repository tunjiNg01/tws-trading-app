import json
import pandas as pd
import requests
import datetime

market_symbol = "btcusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{market_symbol}/"

start = "2023-01-01"
end = "2023-01-02"

dates = pd.date_range(start= start, end= end, freq="1h")

dates = [int(x.value/10**9) for x in list(dates)]

master_data = []
for first, last in zip(dates, dates[1:]):
    print(first, last)

    # print(dates)

    param = {
        "step":60,
        "limit":1000,
        "start":first,
        "end": last
    }

    data = requests.get(url, params = param)

    data = data.json()["data"]["ohlc"]
    master_data += data
    
df = pd.DataFrame(master_data)
df = df.drop_duplicates()
df["timestamp"] = df["timestamp"].astype(int)
df = df.sort_values(by="timestamp")
df = df[df["timestamp"] >= dates[0]]



print(df)