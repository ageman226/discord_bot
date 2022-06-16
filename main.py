from pydoc import cli
import discord
import random
import json

from matplotlib.pyplot import title
import anime as aniPy
import functions as usersFunc
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix= "!", intents=intents)
server = discord.Guild

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def wesley(ctx):
    wesleyQuotes = ["im saving the vampires", "I'm coming on"]
    # user = usersFunc.getUser(ctx, "ageman225")
    quote = random.choice(wesleyQuotes)
    await ctx.send(f"{quote} -wesley")

@client.command(aliases=["topairinganime"])
async def sendAnimeRanks(ctx):
    rankings = aniPy.getAnimeRankingsTop()
    embed = discord.Embed(title="Top Airing Anime", color=0x00ff00)
    embed.set_thumbnail(url=rankings[0]['image'])
    for rank in rankings:
        thisString = f"{rank['title']} [MyAnimeList Page]({aniPy.urlStart}{rank['id']}) "
        embed.add_field(name=rank['rank'], value=thisString, inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=["searchanime"])
async def searchAnime(ctx, *, args):
    search = aniPy.searchAnime(args)
    print(args)
    string = f"{aniPy.urlStart}{search[0]['id']}"
    embed = discord.Embed(title=search[0]["title"], url=string, color=0x00ff00)
    embed.set_thumbnail(url=search[0]["image"])
    if(len(search)==1):
        embed.set_image(url=search[0]["image"])
        embed.add_field(name="Synopsis", value=search[0]["synopsis"], inline=False)
        embed.set_footer(text="Data from myanimelist.net")
        await ctx.send(embed=embed)
    else:
        await ctx.send("There are no results")
        

@client.command(aliases=["8ball", "test"])
async def _8ball(ctx, *, question):
    responses = ["It is certain", "It is decidedly so"]
    author = ctx.author
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}\nAuthor: @{author.mention}\n")

client.run(aniPy.BOTTOKEN)