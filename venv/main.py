import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("", "", True)
    bitmex = BitmexClient("", "", True)

    root = Root(binance, bitmex)
    root.mainloop()

    # Source code to compare. Remember the specific changes for macos
#     import logging

# from connectors.binance import BinanceClient
# from connectors.bitmex import BitmexClient

# from interface.root_component import Root


# # Create and configure the logger object

# logger = logging.getLogger()

# logger.setLevel(logging.DEBUG)  # Overall minimum logging level

# stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
# formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
# stream_handler.setFormatter(formatter)
# stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

# file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)


# if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

#     binance = BinanceClient("",
#                             "",
#                             testnet=True, futures=True)
#     bitmex = BitmexClient("", "", testnet=True)

#     root = Root(binance, bitmex)
#     root.mainloop()

