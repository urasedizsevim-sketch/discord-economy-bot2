import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MY_GUILD_ID = 123456789012345678   #Replace with your Guild ID


def format_number(val: float) -> str:
    if val == 0:
        return "0.00"
    if val >= 1:
        return f"{val:,.2f}"
    else:
        formatted = f"{val:.8f}".rstrip('0')
        return formatted if not formatted.endswith('.') else formatted + "00"


def get_rate(from_curr: str, to_curr: str):
    """Fetches rate for both Fiat currencies and Cryptos dynamically."""
    crypto_map = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "SOL": "solana",
        "DOGE": "dogecoin",
        "XRP": "ripple",
        "BNB": "binancecoin",
        "LTC": "litecoin",
        "USDT": "tether"
    }

    if from_curr in crypto_map:
        coin_id = crypto_map[from_curr]
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={to_curr.lower()}"
        res = requests.get(url).json()
        if coin_id in res and to_curr.lower() in res[coin_id]:
            return res[coin_id][to_curr.lower()]

    url = f"https://open.er-api.com/v6/latest/{from_curr}"
    res = requests.get(url).json()
    if res.get("result") == "success" and to_curr in res["rates"]:
        return res["rates"][to_curr]

    if to_curr in crypto_map:
        coin_id = crypto_map[to_curr]
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={from_curr.lower()}"
        res = requests.get(url).json()
        if coin_id in res and from_curr.lower() in res[coin_id]:
            return 1 / res[coin_id][from_curr.lower()]

    return None


@bot.event
async def on_ready():
    guild = discord.Object(id=MY_GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    synced = await bot.tree.sync(guild=guild)
    print(f"Converter Bot is ready! Synced {len(synced)} slash command(s).")


@bot.tree.command(name="convert", description="Converts live currency & crypto exchange rates.")
async def convert_slash(
    interaction: discord.Interaction,
    amount_input: str,
    from_currency: str,
    to_currency: str
):
    await interaction.response.defer()

    try:
        clean_amount = amount_input.replace(",", ".")
        amount = float(clean_amount)
    except ValueError:
        await interaction.followup.send("Invalid amount format. Please type a valid number (e.g. `0.000025`).", ephemeral=True)
        return

    from_curr = from_currency.upper().replace("TL", "TRY")
    to_curr = to_currency.upper().replace("TL", "TRY")

    try:
        rate = get_rate(from_curr, to_curr)

        if rate is not None:
            result = amount * rate
            reverse_rate = 1 / rate if rate != 0 else 0

            amount_fmt = format_number(amount)
            result_fmt = format_number(result)
            rate_fmt = format_number(rate)
            reverse_fmt = format_number(reverse_rate)

            # --- EMBED CARD ---
            embed = discord.Embed(
                title="Currency & Crypto Converter",
                description=f"**{amount_fmt} {from_curr}** ➔ **{result_fmt} {to_curr}**",
                color=discord.Color.gold()
            )

            embed.add_field(name="Amount", value=f"`{amount_fmt} {from_curr}`", inline=True)
            embed.add_field(name="Result", value=f"`{result_fmt} {to_curr}`", inline=True)
            embed.add_field(name="Exchange Rate", value=f"`1 {from_curr} = {rate_fmt} {to_curr}`", inline=False)

            embed.set_footer(
                text=f"Inverse Rate: 1 {to_curr} = {reverse_fmt} {from_curr} • Live API Data",
                icon_url="https://cdn-icons-png.flaticon.com/512/6001/6001368.png"
            )

            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(
                f"Invalid or unsupported currency pair: `{from_curr}` to `{to_curr}`.",
                ephemeral=True
            )

    except Exception as e:
        await interaction.followup.send(f"An error occurred while fetching exchange rates: {e}", ephemeral=True)


bot.run("YOUR_BOT_TOKEN_HERE")
