from discord.ext import commands
import discord
import random
import webbrowser

class SimpleView(discord.ui.View):
    @discord.ui.button(label="Commands", style=discord.ButtonStyle.blurple)
    async def cmdbtn(self, interaction: discord.Interaction, button:discord.ui.Button, ephemeral=True):
        await interaction.response.send_message(help_string,ephemeral=True)
    @discord.ui.button(label="Youtube", style=discord.ButtonStyle.red)
    async def ytbtn(self, interaction: discord.Interaction, button:discord.ui.Button, ephemeral=True):
        await webbrowser.open('https://www.youtube.com/@Fenrir26')
    @discord.ui.button(label="X", style=discord.ButtonStyle.gray)
    async def xbtn(self, interaction: discord.Interaction, button:discord.ui.Button):
        await webbrowser.open('https://twitter.com/fenrir2608')

TOKEN = 'MTEzNjMzMzc1NTMzOTAwMjA3OA.Gf4beI.v9rt3SCp6wyTB4CwHc9MCVy7W0cwjZDXvB20RM'
generalChannel = 775039954849759238
greetings = [
    'hello',
    'hello there',
    'hey',
    'hi',
    'greetings',
    'howdy',
    "what's up",
    "how's it going",
    'nice to meet you',
    'hi friend',
    'hey buddy',
    'hello friend',
    'hiya mate',
    'hello, my friend',
    'hello, my friend (soviet accent)',
    'greetings and salutations',
    'hiya pal',
    'hello there, friend',
    "how's everything",
    'hiya there',
    'hey there m8',
    'hello m8',
    'hello world',
    'hello everybody',
    'hi everyone',
]
gfreply =[
    "https://media.giphy.com/media/yyVph7ANKftIs/giphy.gif",
    "https://media.giphy.com/media/0218ft4yXkI5O0pNn6/giphy.gif",
    "https://media.giphy.com/media/uKuzJ71SsbZcZ5nT16/giphy.gif",
    "https://media.giphy.com/media/AtlvFkFcxBU2HUadGY/giphy.gif",
    "https://media.giphy.com/media/EvpaQ7YVPCZvG/giphy.gif",
    "https://media.giphy.com/media/AFdcYElkoNAUE/giphy.gif",
    "https://media.giphy.com/media/9cZQnwdzUXTDG/giphy.gif",
    "https://media.giphy.com/media/4TmxH7ZMn1aYE/giphy.gif",
    "https://media.giphy.com/media/PR3wumHIdsBhu/giphy.gif",
    "https://media.giphy.com/media/bqSkJ4IwNcoZG/giphy.gif",
    "https://media.giphy.com/media/cJ5oaMoekxnipcWSPP/giphy.gif",
    "https://media.giphy.com/media/FWAcpJsFT9mvrv0e7a/giphy.gif",
    "https://media.giphy.com/media/ree8xCap5nHi/giphy.gif",
    "https://media.giphy.com/media/VUhn4clMyitnG/giphy.gif",
    "https://media.giphy.com/media/BS5xpdVyMKniU/giphy.gif",
    "https://media.giphy.com/media/ysOtnle4uSbK/giphy.gif",
    "https://media.giphy.com/media/DeBBINXN86r8Q/giphy.gif",
    "https://media.giphy.com/media/3o7btMCltyDvSgF92E/giphy.gif",
    "https://media.giphy.com/media/ZtB2l3jHiJsFa/giphy.gif",
    "https://media.giphy.com/media/862A6X2sooSsw/giphy.gif",
    "https://media.giphy.com/media/rKJwzDhaUpa6I/giphy.gif",
    "https://media.giphy.com/media/oQVGWxM4nsGcYIs05y/giphy.gif",
    "https://tenor.com/bfVsv.gif",
    "https://tenor.com/77Uj.gif",
    "https://tenor.com/brODw.gif",
    "https://tenor.com/biZMK.gif",
    "https://tenor.com/bB3E6.gif",
    "https://tenor.com/bXBvs.gif",
    "https://tenor.com/bl1Kq.gif",
    "https://tenor.com/bSZXg.gif",
    "https://tenor.com/bSzKo.gif"
]
help_string = "`here to help`"
bot = commands.Bot(command_prefix="feni ", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Feni Bot is up and running!")

#general commands
@bot.command()
async def hi(ctx):
    await ctx.reply(random.choice(greetings))

@bot.command()
async def helps(ctx):
    view = SimpleView()
    await ctx.send(view=view, ephemeral=True)

#arithmetic commands
@bot.command()
async def add(ctx,*arr):
    if len(arr) == 0:
        await ctx.reply("pls provide at least one number to add.")
        return
    result = 0
    for i in arr:
        result += int(i)
    await ctx.reply(result)

@bot.command()
async def mul(ctx,*arr):
    if len(arr) == 0:
        await ctx.reply("pls provide at least one number to multiply.")
        return
    result = 1
    for i in arr:
        result = result * int(i)
    await ctx.reply(result)

@bot.command()
async def subs(ctx,*arr):
    if len(arr) == 0:
        await ctx.reply("pls provide at least one number to substract.")
        return
    result = int(arr[0])
    for i in arr[1:]:
        result -= int(i)
    await ctx.reply(result)

@bot.command()
async def div(ctx, *arr):
    if len(arr) == 0:
        await ctx.reply("pls provide at least one number to divide.")
        return

    result = int(arr[0])
    try:
        for i in arr[1:]:
            result /= int(i)
        await ctx.reply(result)
    except ZeroDivisionError:
        await ctx.reply("cannot divide by zero.")

#other commands
@bot.command()
async def gf(ctx):
    await ctx.reply(random.choice(gfreply))
@bot.command()
async def bf(ctx):
    await webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
@bot.command()
async def gif(ctx, search_term):
    apikey = "AIzaSyA573pshtoTYsqfQcpQUXd-rOA4FKDuf2Y"
    lmt = 8
    ckey = "I WANT GIFS"
    #search_term = "excited"
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        print(top_8gifs)
    else:
        top_8gifs = None
    await webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
@bot.command()
async def fenrir(ctx):
    await webbrowser.open('https://www.youtube.com/@Fenrir26')
@bot.command()
async def feni(ctx):
    await webbrowser.open('https://www.youtube.com/@Fenrir26')
bot.run(TOKEN)

# TENOR API KEY = AIzaSyA573pshtoTYsqfQcpQUXd-rOA4FKDuf2Y