import requests
import locale
import schedule
import time
import json

tg_bot_token = '' # Get telegram bot token: @BotFather
chat_id = '' # Get your telegram chat id: @getmyid_bot
local_currency = 'USD' # Enter your local currency. If you don't need it, specify USD
coinmarketcap_api_key = '' # Get ApiKey in https://pro.coinmarketcap.com/account
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def get_price(symbol):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        'X-CMC_PRO_API_KEY': coinmarketcap_api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data'][symbol]['quote']['USD']['price']

def get_rate_to_usd():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    print(data['rates'][local_currency])
    return data['rates'][local_currency]

def send_log(message, tg_bot_token, chat_id):
    url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    print(response.json())
    return response.json()

def format_converted(number):
    return locale.format_string("%d", number, grouping=True)

def load_portfolio(filename='crypto_portfolio.json'):
    with open(filename, 'r') as f:
        portfolio = json.load(f)
    return portfolio

def main_task():
    crypto_portfolio = load_portfolio()

    rate_to_usd = get_rate_to_usd()

    logs = ""
    total_value_usd = 0
    total_value_converted = 0
    for i, (symbol, amount) in enumerate(crypto_portfolio.items(), start=1):
        if symbol == 'USDT':
            price_usd = 1 # USDT always costs $1
        else:
            price_usd = get_price(symbol)
        value_usd = price_usd * amount
        value_converted = value_usd * rate_to_usd
        total_value_usd += value_usd
        total_value_converted += value_converted
        logs += f"{i}\uFE0F\u20E3 {symbol} - {amount} x ${price_usd:.3f}.\n— ${value_usd:.2f} ({format_converted(int(value_converted))} {local_currency})\n\n"

    logs = f"💵 ${total_value_usd:.2f} ({format_converted(int(total_value_converted))} {local_currency})\n\n\n{logs}"

    send_log(logs, tg_bot_token, chat_id)

main_task()
schedule.every().hour.do(main_task)

while True:
    schedule.run_pending()
    time.sleep(1)
