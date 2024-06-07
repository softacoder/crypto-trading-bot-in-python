import tkinter as tk
import logging
# from binance_futures import write_log
# from bitmex import get_contracts

from connectors.binance_futures import BinanceFuturesClient

logger = logging.getLogger()

# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("paste in public_key from binance testnet", "paste in secret_key from binance testnet?", 12)

    candles = binance.get_historical_candles()
    candles[-1]
    

    root = tk.Tk()
    root.mainloop()