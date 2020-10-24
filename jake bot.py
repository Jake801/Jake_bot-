import discord 
from discord.ext import commands
bot = commands.Bot(command_prefix= '.')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('type .help'))
    print("Bot is ready")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def joke(ctx):
   await ctx.send('The floor is lava...3....2.....1.....run!')

@bot.command()
async def give_me_something_to_do(ctx):
    await ctx.send('GO AND CLEAN YOUR ROOM!')

@bot.command()
async def meme(ctx):
    await ctx.send('Memes are not in use with this bot yet they are gonna be worked on soon.')

@bot.command()
async def rate(ctx):
    await ctx.send('You are awesome do not let anyone tell you different!')

@bot.command()
async def give_power(ctx):
    await ctx.send('You can now take over the world!')

@bot.command()
async def mod_wii(ctx):
    await ctx.send('To mod you wii system go to https://wii.guide/riiconnect24')

@bot.command()
async def twitter(ctx):
    await ctx.send('Go follow Jake on twitter: https://twitter.com/SoonTM32')

@bot.command()
async def sucks(ctx):
   await ctx.send('Windows sucks use linux')

@bot.command()
async def nintendo(ctx):
    await ctx.send('What is your favorite nintendo console and why?')

@bot.command()
async def mario(ctx):
    await ctx.send('Its a me Mario Whaoo')

@bot.command()
async def annoy(ctx):
    await ctx.send('Stop you fool! XD')

@bot.command()
async def tom_nook(ctx):
    await ctx.send('Tom nook you are a trash panda!')

@bot.command()
async def bored(ctx):
    await ctx.send('Go and have some fun, enjoy yourself or play music & play games.')

@bot.command()
async def oof(ctx):
    await ctx.send('ssssssss oh no run a creeper is behind you RUN!!!')

@bot.command()
async def Dr(ctx):
    await ctx.send('Come on in and see DR Mario')

@bot.command()
async def what_is_windows(ctx):
    await ctx.send('Windows is a operating system that is developed by Microsoft, the latest Windows OS is Windows 10.')

@bot.command()
async def what_is_discord(ctx):
    await ctx.send('What is discord? You got to be kidding, you are using it right now lol.')

@bot.event
async def on_memeber_join(member):
    print(f'{member} has joined the server make sure you welcome them')

@bot.event
async def on_memeber_remove(member):
    print(f'{member} has left the server they have gone to Mars')

@bot.command()
async def what_is_linux(ctx):
    await ctx.send('Linux is an open source OS and some say its Awesome!')

@bot.command()
async def what_is_life(ctx):
    await ctx.send('Life means that you should have fun, never let anyone get you down!')

@bot.command()
async def youtube(ctx):
    await ctx.send('https://youtube.com')

@bot.command()
async def amazon_US(ctx):
    await ctx.send('https://amazon.com')

@bot.command()
async def amazon_UK(ctx):
   await ctx.send('https://amzon.co.uk')

bot.run('NzY5NTA5ODAxMjIxOTQ3NDEz.X5QD2Q.WkiRe8wlPK6QzDGqINnfn_Q4rII')
