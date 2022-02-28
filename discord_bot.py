import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
bot.remove_command("help")

memes_gifs = ['https://c.tenor.com/hBj6FUyDpI0AAAAd/steal-memes.gif', 'https://c.tenor.com/yjeq2j32A0gAAAAi/hmm-rotating.gif', 'https://c.tenor.com/ZATOt03poKUAAAAd/spongebob-spongebob-meme.gif']
laugh_gifs = ['https://c.tenor.com/BP9vMzwRSZwAAAAC/laughing-lol.gif', 'https://c.tenor.com/fqRNsILmXHQAAAAM/anime-girl.gif', 'https://c.tenor.com/XbGebOy9Lf0AAAAC/anime-girl.gif', 'https://c.tenor.com/GwJ2vJ1gnfcAAAAC/anime-anime-laughing.gif', 'https://tenor.com/view/huhuhu-anime-cute-laugh-gif-14725878']
skull_gifs = ['https://c.tenor.com/KK4vdOwqsQYAAAAC/bruh.gif', 'https://c.tenor.com/jeYb8iK3YfsAAAAi/skull-skullgif.gif', 'https://c.tenor.com/Nghi4vHCe34AAAAi/android-meme.gif']
skull_names = ['is dead']

@bot.command()
async def eecs1720(ctx):
    await ctx.reply('This course continues an introduction to computer programming within the context of image, sound and interaction, subsequent to EECS1710 3.00. The student’s foundation in basic programming will serve as a platform from which to explore the use of diverse media within interactive systems, including the WWW and simple game systems.  https://www.eecs.yorku.ca/course_archive/2016-17/W/1720/')

@bot.command()
async def syllabus(ctx):
    await ctx.reply('https://www.eecs.yorku.ca/course_archive/2021-22/W/1720/EECS1720_2022w_syllabus.pdf')

@bot.command()
async def repo(ctx):
    await ctx.reply('https://github.com/robots-make-art-too')

@bot.command()
async def lecture(ctx):
    await ctx.reply('https://yorku.zoom.us/j/94867212941?pwd=dEtkc0IrSUp5MXQ5dzlZN0NvUXZQQT09')

@bot.command()
async def poll(ctx,*,message):
    emb=discord.Embed(title=" POLL ", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')



@bot.command()
async def memes(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
    )
    embed.set_image(url=(random.choice(memes_gifs)))

    await ctx.send(embed=embed)

@bot.command()
async def skull(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(skull_names))}"
    )
    embed.set_image(url=(random.choice(skull_gifs)))

    await ctx.send(embed=embed)

@bot.command()
async def laugh(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} is laughing"

    )
    embed.set_image(url=(random.choice(laugh_gifs)))

    await ctx.send(embed=embed)

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Welcome to the EECS Bot, here are all the commands you could use!")
    em.add_field(name = "?eecs1720", value = "Gives information on the course 'EECS 1720'")
    em.add_field(name = "?syllabus", value = "Gives the link to the syllabus for EECS 1720")
    em.add_field(name = "?repo", value = "Gives the link to the EECS 1720 Repo")
    em.add_field(name = "?lecture", value = "Gives the link to the EECS 1720 lecture")
    em.add_field(name = "?laugh", value = "Way to show laughter")
    em.add_field(name = "?skull", value = "Better way to show laughter")
    em.add_field(name = "?memes", value = "Random Memes")
    em.add_field(name = "?poll", value = "Creates a voting poll")



    await ctx.send(embed = em)





bot.run('OTQ3NjY5NzE3MzExNjg4Nzg2.YhwoMw.q-wEBxkNUxSe6c9Oebveru5yEN0')