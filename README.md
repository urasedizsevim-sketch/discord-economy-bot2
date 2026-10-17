# Real-Time Currency and Crypto Exchange Converter Discord Bot

A reliable and lightweight Discord bot built in Python to convert fiat currencies and cryptocurrencies in real-time using live exchange rate APIs. Designed with native Slash Commands and a clean Embed UI output.

![Python](https://img.shields.io/badge/python-v3.10%2B-blue?style=flat-square&logo=python)
![discord.py](https://img.shields.io/badge/discord.py-v2.0%2B-blue?style=flat-square&logo=discord)
![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)

---

## Features

- **Live Fiat Rates:** Fetches real-time financial market rates via Open Exchange Rates API.
- **Cryptocurrency Support:** Integrates CoinGecko API to fetch live prices for popular cryptos (BTC, ETH, SOL, DOGE, XRP, BNB, LTC, USDT, etc.).
- **Modern Slash Commands:** Built using Discord's Application Commands API (`/convert`).
- **Structured Embed UI:** Displays conversion results, direct rates, and inverse rates in a clean, professional layout.
- **Smart Number Formatting:** Automatically formats large fiat values with commas and displays small crypto values perfectly without scientific notation (e.g., `0.00000025`).
- **Input Normalization & Error Handling:** Auto-capitalizes currency inputs, maps local aliases (e.g., TL to TRY), and handles invalid currency codes gracefully.

---

## Tech Stack

- **Language:** Python 3
- **Library:** `discord.py` (v2.0+)
- **APIs:** Open Exchange Rates API (`open.er-api.com`) & CoinGecko API (`api.coingecko.com`)
- **HTTP Client:** `requests`

---

## Command Usage

| Command | Arguments | Description | Example |
| :--- | :--- | :--- | :--- |
| `/convert` | `amount_input`, `from_currency`, `to_currency` | Converts an amount between specified fiat or crypto currencies in real-time. | `/convert amount_input:100 from_currency:USD to_currency:BTC` |

---

## Preview

![Bot Preview](./demo2.jpg)

---

## Custom Bot Commissions

Looking for a custom Discord bot tailored for your server, community, or business?  
Feel free to reach out for custom development inquiries.

**Discord:** `uras0402_95891`
