import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_cryptocurrency_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from CoinGecko API. Status code: {response.status_code}")

def process_data(raw_data):
    df = pd.DataFrame(raw_data)
    df = df[['id', 'symbol', 'name', 'market_cap']]
    df = df.sort_values(by='market_cap', ascending=False).head(10)
    return df

def plot_data(df):
    plt.figure(figsize=(12, 6))
    plt.bar(df['symbol'], df['market_cap'], color='skyblue', edgecolor='black', width=0.6)
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Market Cap (USD)')
    plt.title('Top 10 Cryptocurrencies by Market Cap')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    try:
        raw_data = fetch_cryptocurrency_data()
        df = process_data(raw_data)
        plot_data(df)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
