import json, requests
from Data_Collection import key_parser

try:
    api_key = key_parser.parse()['alpha vantage']
except KeyError:
    print('Error parsing key file: Alpha Vantage key missing. Make sure to create a key file with the necessary api keys.')

def request(params, saveAs=''):
    url = 'https://www.alphavantage.co/query?'
    try:
        params['apikey'] = api_key
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        print(data)
        if saveAs:
            json.dump(data, open(saveAs, 'w'))
    except Exception as e:
        print('Invalid Request. This is likely due to incorrect input parameters')
        print(e)

def info():
    print('For more information on what parameters to use see https://www.alphavantage.co/documentation/')

