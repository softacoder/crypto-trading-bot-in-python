import tkinter as tk
import logging
# from binance_futures import write_log
# from bitmex import get_contracts

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

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

    

    binance = BinanceFuturesClient("paste in public_key from binance testnet", "paste in secret_key from binance testnet?", True)

    bitmex = BitmexClient("paste in public_key from bitmex testnet", "paste in secret_key from bitmex testnet?" , True)

    print(bitmex.place_order(bitmex.contract['XBTUSD'], "Limit", 100, "Buy", 20000.4939338, "GoodTillCancel"))
          
    root = tk.Tk()
    root.mainloop()