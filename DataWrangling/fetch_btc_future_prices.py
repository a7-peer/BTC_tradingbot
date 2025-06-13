import requests
import pandas as pd
from datetime import datetime

# Function to convert date string to milliseconds since epoch
def date_to_millis(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int(dt.timestamp() * 1000)

# Function to fetch all future klines data within a date range
def fetch_future_prices(start_date, end_date):
    start_time = date_to_millis(start_date)
    end_time = date_to_millis(end_date)
    all_data = []

    limit = 1000  # Max number of data points per request

    while start_time < end_time:
        url = "https://fapi.binance.com/fapi/v1/klines"
        params = {
            "symbol": "BTCUSDT",
            "interval": "1d",
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit
        }

        response = requests.get(url, params=params)
        data = response.json()

        if not data:
            break

        # Append data
        all_data.extend(data)

        # Update start_time to just after last candle's open time
        last_time = data[-1][0]
        start_time = last_time + 1

        # If fewer than limit is returned, we've fetched all data
        if len(data) < limit:
            break

    return all_data

# Main execution
start_date = "2019-02-02"
end_date = datetime.now().strftime("%Y-%m-%d")

print(f"Fetching Bitcoin futures prices from {start_date} to {end_date}...")
data = fetch_future_prices(start_date, end_date)
print(f"Fetched {len(data)} data points.")

# Extract date and close price only
records = []
for entry in data:
    open_time = datetime.fromtimestamp(entry[0] / 1000).strftime('%Y-%m-%d')
    close_price = float(entry[4])
    records.append({"date": open_time, "close": close_price})

# Convert to DataFrame
df = pd.DataFrame(records)
print(df.head())  # show first few rows

# Optional: Save to CSV
df.to_csv("closeFUT.csv", index=False)
print("Data saved to 'future_prices_btc_2019_to_today.csv'")