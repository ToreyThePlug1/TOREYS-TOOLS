import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is ready.')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_server(ctx):
    guild = ctx.guild

    # Create Custom Roles
    roles = {
        "Admin": discord.Permissions(administrator=True),
        "Moderator": discord.Permissions(manage_messages=True, kick_members=True, ban_members=True),
        "Member": discord.Permissions(read_messages=True, send_messages=True),
        "VIP": discord.Permissions(read_messages=True, send_messages=True, priority_speaker=True),
        "Muted": discord.Permissions(send_messages=False, speak=False)
    }

    created_roles = {}
    for role_name, perms in roles.items():
        role = await guild.create_role(name=role_name, permissions=perms)
        created_roles[role_name] = role

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
        "Call of Duty: World at War": ["codwaw-discussion", "codwaw-voice-chat"],
        "Call of Duty: Modern Warfare 2": ["codmw2-discussion", "codmw2-voice-chat"],
        "Call of Duty: Black Ops": ["codbo-discussion", "codbo-voice-chat"],
        "Call of Duty: Modern Warfare 3": ["codmw3-discussion", "codmw3-voice-chat"],
        "Call of Duty: Black Ops II": ["codbo2-discussion", "codbo2-voice-chat"],
        "Call of Duty: Ghosts": ["codghosts-discussion", "codghosts-voice-chat"],
        "Call of Duty: Advanced Warfare": ["codaw-discussion", "codaw-voice-chat"],
        "Call of Duty: Black Ops III": ["codbo3-discussion", "codbo3-voice-chat"],
        "Call of Duty: Infinite Warfare": ["codiw-discussion", "codiw-voice-chat"],
        "Call of Duty: Modern Warfare Remastered": ["codmwr-discussion", "codmwr-voice-chat"],
        "Call of Duty: WWII": ["codwwii-discussion", "codwwii-voice-chat"],
        "Call of Duty: Black Ops 4": ["codbo4-discussion", "codbo4-voice-chat"],
        "Call of Duty: Black Ops Cold War": ["codcoldwar-discussion", "codcoldwar-voice-chat"],
        "Call of Duty: Vanguard": ["codvanguard-discussion", "codvanguard-voice-chat"],
        "Call of Duty: Modern Warfare II": ["codmw2-2022-discussion", "codmw2-2022-voice-chat"],
        "Call of Duty: Modern Warfare III": ["codmw3-2023-discussion", "codmw3-2023-voice-chat"],
        "Call of Duty: Black Ops 6": ["codbo6-discussion", "codbo6-voice-chat"],
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

    # Create Admin & Mod Channels with specific role permissions
    admin_channels = ["admin-chat", "mod-chat", "admin-announcements"]
    admin_cat = await guild.create_category("Admin & Mod Channels")
    for channel in admin_channels:
        text_channel = await guild.create_text_channel(channel, category=admin_cat)
        if channel == "admin-chat" or channel == "admin-announcements":
            await text_channel.set_permissions(created_roles["Admin"], read_messages=True, send_messages=True)
            await text_channel.set_permissions(guild.default_role, read_messages=False)
        if channel == "mod-chat":
            await text_channel.set_permissions(created_roles["Admin"], read_messages=True, send_messages=True)
            await text_channel.set_permissions(created_roles["Moderator"], read_messages=True, send_messages=True)
            await text_channel.set_permissions(guild.default_role, read_messages=False)

    await ctx.send("Server setup complete!")

bot.run('YOUR_BOT_TOKEN')
