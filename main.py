import os
import discord
from discord.ext import commands
import openai

# Load API keys from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY

# Set up Discord intents
intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

# Create bot instance
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")

@bot.command()
async def chat(ctx, *, message):
    """Chat with ChatGPT using /chat <message>"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=500
        )
        reply = response.choices[0].message.content
        await ctx.send(reply)
    except Exception as e:
        await ctx.send(f"Error: {e}")

# Run the bot
bot.run(DISCORD_TOKEN)
