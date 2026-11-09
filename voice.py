import nextcord
from nextcord.ext import commands
import os

# Discord Server and Voice Channel
BotSever1 = 1196284152329277510  # Discord Server ID
BotSever2 = 1196284153180737540  # Voice Channel ID

# Bot Intents
intents = nextcord.Intents.default()
intents.message_content = True
intents.voice_states = True

# Create Bot
bot = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=intents
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

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
            f'{member.name} is in '
            f'{after.channel.name} and started streaming.'
        )

# Get Discord Token from Environment
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN environment variable is missing.")

bot.run(TOKEN)
