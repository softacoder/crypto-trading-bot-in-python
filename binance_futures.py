import logging
import requests

logger = logging.getLogger()


def get_contracts():

    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(response_object.status_code)
    pprint.pprint(response_object.json()['symbols'])

    for contract in response_object.json()['symbol']:
        pprint.pprint(contract)
        print(contract['pair'])
        contract.append(contract['pair'])

    return contracts

print(get_contracts())

