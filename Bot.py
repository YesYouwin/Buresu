import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Sync slash commands
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"Logged in as {bot.user}")


# SCRIM COMMAND
@bot.tree.command(name="scrim", description="Create a Valorant scrim schedule")

@app_commands.describe(
    scrim_type="Type of scrim",
    team1="First team role",
    team2="Second team role",
    time="Match time (example: 7:30PM)",
    date="Date (DD/MM/YYYY)",
    map_name="Map name",
    timezone="Select timezone"
)

@app_commands.choices(
    timezone=[
        app_commands.Choice(name="IST", value="IST"),
        app_commands.Choice(name="SGT", value="SGT"),
        app_commands.Choice(name="GMT", value="GMT"),
        app_commands.Choice(name="PHT", value="PHT"),
    ]
)

async def scrim(
    interaction: discord.Interaction,
    scrim_type: str,
    team1: discord.Role,
    team2: discord.Role,
    time: str,
    date: str,
    map_name: str,
    timezone: app_commands.Choice[str]
):

    embed = discord.Embed(
        color=discord.Color.red()
    )

    embed.description = f"""
🆚 **Teams**
{team1.mention} **VS** {team2.mention}

📌 **Scrim Type**
{scrim_type}

🕒 **Time**
{time} {timezone.value}

📅 **Date**
{date}

🗺 **Map**
{map_name}

⚠ **Note**
The **IGL** of the team is responsible for any player's absence.
Players must inform beforehand so the scrim runs smoothly.
"""

    embed.set_footer(text="Scrim Manager")

    await interaction.response.send_message(
        content=f"## 🎮 SCRIM SCHEDULE\n{team1.mention} {team2.mention}",
        embed=embed
    )


bot.run(TOKEN)
