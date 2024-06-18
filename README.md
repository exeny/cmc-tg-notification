<h1 align="center"> CoinMarketCap Portfolio Notification </h1>
<h3 align="center"> (Telegram Bot) </h3>
</br>
<p align="center">
<a href="#"><img src="https://img.shields.io/github/license/exeny/cmc-tg-notification.svg?style=flat-square" alt="License"></a>
<a href="https://scrutinizer-ci.com/g/exeny/cmc-tg-notification"><img src="https://img.shields.io/scrutinizer/g/exeny/cmc-tg-notification" alt="Quality Score"></a>
<a href="https://codeclimate.com/github/exeny/cmc-tg-notification/maintainability"><img src="https://api.codeclimate.com/v1/badges/8cf0f553f611dd558ebe/maintainability"/></a></p>
<p align="center"><a href="t.me/e_xeny"><img src="https://img.shields.io/badge/DEVELOPED%20BY%20Exeny-000000?style=for-the-badge"></a></p>

## Overview

> When launched, it sends a notification with the current portfolio status, and then

- Runs every hour (by default)

### Example of how the bot works

> Need to configurate

> (The first image is a bot working without converting to local currency.
> The second picture is a bot working with currency conversion. )

<p>
<img style="width:100;" src="https://i.imgur.com/Pj2z06o.png"/>
<img style="width:100;" src="https://i.imgur.com/cVizPy6.png"/>
</p>

### Installation

```sh
git clone https://github.com/exeny/cmc-tg-notification.git
cd cmc-tg-notification
pip install -r requirements.txt
```

### Configuration

**Getting your Telegram Bot API Key:**

> Settings are made directly in the cmcportfoliobot.py file.
> The very first step requires you to obtain a valid Telegram Bot API key:

1. Visit [https://t.me/BotFather](https://t.me/BotFather) and send /newbot (then follow the bot's instructions).
2. Done! Enter the API key in tg_bot_token

**Getting chat id:**

1. Visit [https://t.me/getmyid_bot](https://t.me/getmyid_bot) and send /start.
2. Copy your **user id**
3. Enter the chat id in chat_id

**Getting CMC API Key:**

1. Sign Up in [https://pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account) and copy your api key
2. Enter the API key in coinmarketcap_api_key

**Enter coins from your portfolio to this form**

<img src="https://i.imgur.com/1OHTA2x.png">

**Enter local_currency (if you need it)**
<img src="https://i.imgur.com/nBFTGYP.png">
