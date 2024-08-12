import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is ready.')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_server(ctx):
    guild = ctx.guild

    # Create Cannabis Strains Categories and Channels
    strains = {
        "Indica Strains": ["northern-lights", "purple-kush", "granddaddy-purple", "blue-cheese", "hindu-kush"],
        "Sativa Strains": ["sour-diesel", "green-crack", "jack-herer", "durban-poison", "strawberry-cough"],
        "Hybrid Strains": ["blue-dream", "girl-scout-cookies", "pineapple-express", "white-widow", "gg4"]
    }
    for category, channels in strains.items():
        cat = await guild.create_category(category)
        for channel in channels:
            await guild.create_text_channel(channel, category=cat)

    # Create Weed Seed Resources Category and Channels
    seed_resources = ["best-indica-seed-sources", "best-sativa-seed-sources", "best-hybrid-seed-sources", "seed-deals-and-discounts", "growing-tips"]
    seed_cat = await guild.create_category("Weed Seed Resources")
    for channel in seed_resources:
        await guild.create_text_channel(channel, category=seed_cat)

    # Create Gaming Categories and Channels
    games = {
        "Call of Duty 4: Modern Warfare": ["cod4mw-discussion", "cod4mw-voice-chat"],
        # Add other Call of Duty titles here similarly...
        "Fortnite": ["fortnite-discussion", "fortnite-voice-chat"],
        "Arma Reforger": ["arma-reforger-discussion", "arma-reforger-voice-chat"],
        "DCS": ["dcs-discussion", "dcs-voice-chat"]
    }
    for category, channels in games.items():
        cat = await guild.create_category(category)
        for channel in channels:
            if "voice-chat" in channel:
                await guild.create_voice_channel(channel, category=cat)
            else:
                await guild.create_text_channel(channel, category=cat)

    # Create General Channels
    general_channels = ["welcome", "rules", "announcements", "general-chat", "off-topic", "server-suggestions", "support"]
    for channel in general_channels:
        await guild.create_text_channel(channel)

    # Create Admin & Mod Channels
    admin_channels = ["admin-chat", "mod-chat", "admin-announcements"]
    admin_cat = await guild.create_category("Admin & Mod Channels")
    for channel in admin_channels:
        await guild.create_text_channel(channel, category=admin_cat)

    await ctx.send("Server setup complete!")

bot.run('YOUR_BOT_TOKEN')
