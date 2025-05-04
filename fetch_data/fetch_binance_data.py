import ccxt
import pandas as pd


def fetch_binance_ohlcv_data(symbol='BTC/USDT', timeframe='1m', limit=1000):
    """
    Fetches OHLCV data from Binance using the ccxt library.

    Converts the timestamp from Unix epoch (ms) to a UTC datetime index.

    Args:
        symbol (str): Trading pair symbol (e.g., 'BTC/USDT').
        timeframe (str): Candlestick interval (e.g., '1m', '5m', '1h').
        limit (int): Number of candles to fetch (max 1000 per request).

    Returns:
        pd.DataFrame: DataFrame indexed by UTC timestamp with columns:
            ['open', 'high', 'low', 'close', 'volume'].

    Example:
        >>> df = fetch_binance_data('BTC/USDT', '1m', 1000)

    References:
        Binance API via CCXT: https://docs.ccxt.com/#/exchanges/binance
    """
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit, params = {"paginate": True})
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

