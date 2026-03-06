import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

    print(f"Logged in as {bot.user}")


@bot.tree.command(name="scrim", description="Create a Valorant scrim schedule")

@app_commands.describe(
    scrim_type="Scrim Type",
    team_a="TeamA",
    team_b="TeamB",
    time="Match Time (Example: 7:30 PM)",
    timezone="Timezone",
    date="Day / Date",
    map="Select Map",
    format="Match Format",
    team_a_role="Ping Role for TeamA (Optional)",
    team_b_role="Ping Role for TeamB (Optional)"
)

# SCRIM TYPE DROPDOWN
@app_commands.choices(scrim_type=[
    app_commands.Choice(name="In-Houses", value="In-Houses"),
    app_commands.Choice(name="Scrim", value="Scrim"),
    app_commands.Choice(name="Tournament", value="Tournament")
])

# TIMEZONE DROPDOWN
@app_commands.choices(timezone=[
    app_commands.Choice(name="IST", value="IST"),
    app_commands.Choice(name="SGT", value="SGT"),
    app_commands.Choice(name="GMT", value="GMT"),
    app_commands.Choice(name="PST", value="PST")
])

# MAP DROPDOWN
@app_commands.choices(map=[
    app_commands.Choice(name="Ascent", value="Ascent"),
    app_commands.Choice(name="Bind", value="Bind"),
    app_commands.Choice(name="Haven", value="Haven"),
    app_commands.Choice(name="Split", value="Split"),
    app_commands.Choice(name="Lotus", value="Lotus"),
    app_commands.Choice(name="Sunset", value="Sunset"),
    app_commands.Choice(name="Icebox", value="Icebox"),
    app_commands.Choice(name="Breeze", value="Breeze")
])

# FORMAT DROPDOWN
@app_commands.choices(format=[
    app_commands.Choice(name="BO1", value="BO1"),
    app_commands.Choice(name="BO3", value="BO3"),
    app_commands.Choice(name="BO5", value="BO5")
])

async def scrim(
    interaction: discord.Interaction,
    scrim_type: app_commands.Choice[str],
    team_a: str,
    team_b: str,
    time: str,
    timezone: app_commands.Choice[str],
    date: str,
    map: app_commands.Choice[str],
    format: app_commands.Choice[str],
    team_a_role: discord.Role | None = None,
    team_b_role: discord.Role | None = None
):

    # Role pings
    pings = ""
    if team_a_role:
        pings += f"{team_a_role.mention} "
    if team_b_role:
        pings += f"{team_b_role.mention}"

    message = f"""
# 🗓️ SCRIM SCHEDULE

> **Scrim Type:** {scrim_type.value}
> **Teams:** {team_a} **Vs** {team_b}
> **Time:** {time} {timezone.value}
> **Day/Date:** {date}
> **Map:** {map.value}
> **Format:** {format.value}

> **Note:**  
> The @IGL of the team is responsible for any player's absence and the player must inform beforehand about his absence so that the event may run flawlessly.
"""

    await interaction.response.send_message(
        f"{pings}\n{message}",
        allowed_mentions=discord.AllowedMentions(roles=True)
    )


bot.run(TOKEN)
