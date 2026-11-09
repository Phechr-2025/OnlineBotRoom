import nextcord
from nextcord.ext import commands
import os

# Environment Variables
BotSever1 = int(os.getenv("DISCORD_SERVER_ID", "0"))
BotSever2 = int(os.getenv("DISCORD_VOICE_CHANNEL_ID", "0"))
TOKEN = os.getenv("DISCORD_TOKEN")

# Validate Environment
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing.")

if not BotSever1 or not BotSever2:
    raise RuntimeError("Discord Server ID or Voice Channel ID is missing.")

# Bot Intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix="!",
    help_command=None,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    await bot.change_presence(
        activity=nextcord.Streaming(
            name="Phakaphop",
            url="https://www.twitch.tv/phakaphpop"
        )
    )

    guild = bot.get_guild(BotSever1)

    if guild is None:
        print("Error: Discord Server not found.")
        return

    vc = guild.get_channel(BotSever2)

    if vc is None:
        print("Error: Voice Channel not found.")
        return

    await vc.guild.change_voice_state(
        channel=vc,
        self_mute=False,
        self_deaf=True
    )

    print("Bot is ready.")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.self_stream:
        print(
            f"{member.name} is in "
            f"{after.channel.name} and started streaming."
        )

bot.run(TOKEN)
